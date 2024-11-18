from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth.models import User

from .models import Order
from user_profile.models import UserProfile, Trip
from rooms.models import Room
import stripe
import time
import json
from datetime import timedelta, datetime


class StripeWH_Handler:
    '''Handle Stripe Webhooks'''

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        '''Send the user a confirmation email'''
        customer_email = order.email
        # Get the trip
        trip = Trip.objects.get(profile=order.user_profile)
        # Render the email subject as a string and pass the order
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            # This is how we will render the various context variables
            {'order': order, 'trip': trip}
        )
        # Render the email body as a string and pass the order
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            # This is how we will render the various context variables
            {
                'order': order,
                'trip': trip,
                'contact_email': settings.DEFAULT_FROM_EMAIL
            }
        )
        # Send the email using subject, body, email to send from
        # and email to send to
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [customer_email]
        )

    def handle_event(self, event):
        '''Handle a generic/unknown/unexpected webhook event'''
        return HttpResponse(
            content=f'Unhandled Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        '''Handle the payment_intent.succeeded webhook event'''
        # Get the payment intent and all meta data
        intent = event.data.object
        metadata = intent.get('metadata', {})
        pid = intent.id
        trip_data_json = metadata.get('trip_data', '{}')
        trip_data = json.loads(trip_data_json)
        start_date = datetime.strptime(
            trip_data['start_date'],
            '%Y-%m-%d').date()
        end_date = datetime.strptime(trip_data['end_date'], '%Y-%m-%d').date()
        save_info = metadata.get('save_info')
        username = metadata.get('username')

        # Get the user if they are logged in
        user = None
        if username:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                user = None

        # Get the charge object
        stripe_charge = stripe.Charge.retrieve(intent.latest_charge)
        billing_details = stripe_charge.billing_details
        shipping_details = stripe_charge.shipping
        grand_total = round(intent.stripe_charge.amount / 100, 2)

        # Replace empty data in shipping details with None
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Update profile information if save_info was checked
        if user:
            user_profile = None
            if user.is_authenticated:
                user_profile = UserProfile.objects.get(user=user)
                if save_info:
                    user_profile.full_name = shipping_details.name
                    user_profile.phone_number = shipping_details.phone
                    user_profile.country = shipping_details.address.country
                    user_profile.postcode = (
                        shipping_details.address.postal_code
                    )
                    user_profile.town_or_city = shipping_details.address.city
                    user_profile.street_address1 = (
                        shipping_details.address.line1
                    )
                    user_profile.street_address2 = (
                        shipping_details.address.line2
                    )
                    user_profile.county = shipping_details.address.state
                    user_profile.save()
        # Check if order exists, if it does, it's fine, if not, make it
        order_exists = False
        attempt = 1
        while attempt <= 5:
            # Get order info from payment intent (billing details in js)
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    order_total=grand_total,
                    stripe_pid=pid,
                )

                # If order exists, return 200 response
                # Or wait 1 second and try again (max 5 times)
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
                # Create the order if it does not exist
        if order_exists:
            # Send confirmation email
            self._send_confirmation_email(order)
            return HttpResponse(
                    content=(
                        f'Webhook received: {event["type"]} || '
                        f'SUCCESS: Verified order already in database'
                    ), status=200
                )
        else:
            order = None
            try:
                order_form_data = {
                    'user_profile': user_profile,
                    'full_name': shipping_details.name,
                    'email': billing_details.email,
                    'phone_number': shipping_details.phone,
                    'country': shipping_details.address.country,
                    'postcode': shipping_details.address.postal_code,
                    'town_or_city': shipping_details.address.city,
                    'street_address1': shipping_details.address.line1,
                    'street_address2': shipping_details.address.line2,
                    'county': shipping_details.address.state,
                    'order_total': grand_total,
                    'stripe_pid': pid,
                }

                # Create an order instance
                order_instance = Order(**order_form_data)
                order_instance.save()
            # If anything goes wrong, delete and 500 error
            except Exception as e:
                if order_instance:
                    order_instance.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} || ERROR: {e}',
                    status=500)
        # Create a trip instance
        if user.is_authenticated:
            user_profile = UserProfile.objects.get(user=user)
            trip_form_data = {
                'profile': user_profile,
                'room': trip_data.get('room'),
                'start_date': start_date,
                'end_date': end_date,
                'adults': trip_data.get('adults'),
                'children': trip_data.get('children'),
                'infants': trip_data.get('infants'),
                'cost': grand_total,
            }
            trip_instance = Trip(**trip_form_data)
            trip_instance.save()

        # Add unavailable dates to the room
        # Get the room id from the trip_data metadata
        room_booked_id = trip_data.get('room')
        room_booked = Room.objects.get(id=room_booked_id)
        # Get all the unavailable dates
        room_booked_unavailable_dates = json.loads(room_booked.unavailability)
        # Get check in/out dates
        start_date = start_date
        end_date = end_date
        # List for the new dates
        new_dates = []
        # < so that the check out date is not added
        # check out date can be next guests check in date
        # due to check in/out times
        while start_date < end_date:
            # String the date
            date_str = start_date.strftime('%Y-%m-%d')
            # Check if it's not already in unavaiable dates
            if date_str not in room_booked_unavailable_dates:
                # Add to new date
                new_dates.append(date_str)
            # Increment the date by 1 day
            start_date += timedelta(days=1)
        # Combine old and new dates
        updated_dates = room_booked_unavailable_dates + new_dates
        # Add combined to the room unavailability
        room_booked.unavailability = json.dumps(updated_dates)
        room_booked.save()

        # Send confirmation email
        self._send_confirmation_email(order)
        return HttpResponse(
            content=(
                f'Webhook received: {event["type"]} | '
                f'SUCCESS: Created order in webhook'
                ),
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        '''Handle the payment_intent.payment_failed webhook event'''
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
