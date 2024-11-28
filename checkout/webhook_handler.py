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

# Logging
import logging


class StripeWH_Handler:
    '''Handle Stripe Webhooks'''

    def __init__(self, request):
        self.request = request
        self.logger = logging.getLogger('stripe_webhook')

    def _send_confirmation_email(self, order, trip):
        '''Send the user a confirmation email'''
        print("DEBUG: SENDING EMAIL ORDER:", order)
        customer_email = order.email
        print("DEBUG: SENDING CUSTOMER EMAIL")
        print("DEBUG: CUSTOMER EMAIL:", customer_email)
        print("DEBUG: TRIP:", trip)
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
        print("DEBUG: SENDING EMAIL")
        self.logger.debug("Sending confirmation email to: " + customer_email)
        try:
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [customer_email]
            )
            self.logger.debug("Confirmation email sent to: " + customer_email)
            print("DEBUG: EMAIL SENT")
        except Exception as e:
            self.logger.error(f"Error sending email: {str(e)}")
            print("DEBUG: EMAIL ERROR")

    def create_trip(
            self,
            user,
            profile,
            room_id,
            start_date,
            end_date,
            adults,
            children,
            infants,
            cost):
        '''Create a trip instance'''
        print("DEBUG: CREATING TRIP FUNCTION")
        room = Room.objects.get(id=room_id)
        print("DEBUG: GETTING ROOM:", room)
        trip_form_data = {
            'profile': profile,
            'room': room,
            'start_date': start_date,
            'end_date': end_date,
            'adults': adults,
            'children': children,
            'infants': infants,
            'cost': cost,
        }
        print("DEBUG: TRIP FORM DATA:", trip_form_data)
        trip_instance = Trip(**trip_form_data)
        print("DEBUG: TRIP INSTANCE:", trip_instance)
        trip_instance.save()
        print("DEBUG: TRIP SAVED")
        return trip_instance

    def update_room(self, room_id, start_date, end_date):
        '''Update the room unavailability upon order'''
        print("DEBUG: UPDATING ROOM FUNCTION")
        # Get the room
        room_booked = Room.objects.get(id=room_id)
        print("DEBUG: ROOM BOOKED:", room_booked)
        # Get all the unavailable dates
        room_booked_unavailable_dates = json.loads(room_booked.unavailability)
        print("DEBUG: ROOM BOOKED UNAVAILABLE DATES:", room_booked_unavailable_dates)
        # Get check in/out dates
        start_date = start_date
        end_date = end_date
        print("DEBUG: START DATE:", start_date)
        print("DEBUG: END DATE:", end_date)
        # List for the new dates
        new_dates = []
        print("DEBUG: NEW DATES:", new_dates)
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
        print("DEBUG: UPDATED DATES:", updated_dates)
        # Add combined to the room unavailability
        room_booked.unavailability = json.dumps(updated_dates)
        print("DEBUG: ROOM BOOKED UNAVAILABILITY:", room_booked.unavailability)
        room_booked.save()
        print("DEBUG: ROOM BOOKED SAVED")

    def handle_event(self, event):
        '''Handle a generic/unknown/unexpected webhook event'''
        return HttpResponse(
            content=f'Unhandled Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        '''Handle the payment_intent.succeeded webhook event'''
        self.logger.info(f"Received Stripe webhook: {self.request.body}")
        print("DEBUG: PAYMENT INTENT SUCCEEDED")
        # Get the payment intent and all meta data
        intent = event.data.object
        print("DEBUG: INTENT:", intent)
        metadata = intent.get('metadata', {})
        print("DEBUG: METADATA:", metadata)
        pid = intent.id
        print("DEBUG: PID:", pid)
        trip_data_json = metadata.get('trip_data', '{}')
        trip_data = json.loads(trip_data_json)
        print("DEBUG: TRIP DATA JSON:", trip_data_json)
        print("DEBUG: TRIP DATA:", trip_data)
        start_date = trip_data['start_date']
        end_date = trip_data['end_date']
        print("DEBUG: START DATE:", start_date)
        print("DEBUG: END DATE:", end_date)
        print("DEBUG: ROOM:", trip_data['room'])

        # start_date = datetime.strptime(
        #     trip_data['start_date'],
        #     '%Y-%m-%d').date()
        # end_date = datetime.strptime(trip_data['end_date'], '%Y-%m-%d').date()
        save_info = metadata.get('save_info')
        print("DEBUG: SAVE INFO:", save_info)
        email = metadata.get('user_email')
        print("DEBUG: EMAIL:", email)

        # Get the user if they are logged in
        user = None
        print("DEBUG: User none:", user)
        if email:
            user = User.objects.get(email=email)
            print("DEBUG: User:", user)

        # Get the charge object
        stripe_charge = stripe.Charge.retrieve(intent.latest_charge)
        print("DEBUG: STRIPE CHARGE:", stripe_charge)
        billing_details = stripe_charge.billing_details
        print("DEBUG: BILLING DETAILS:", billing_details)
        shipping_details = stripe_charge.shipping
        print("DEBUG: SHIPPING DETAILS:", shipping_details)
        grand_total = round(stripe_charge.amount / 100, 2)
        print("DEBUG: GRAND TOTAL:", grand_total)

        # Replace empty data in shipping details with None
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Update profile information if save_info was checked
        if user:
            print("DEBUG: UPDATING USER INFO")
            user_profile = None
            if user.is_authenticated:
                user_profile = UserProfile.objects.get(user=user)
                print("DEBUG: USER", user_profile)
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
                    print("DEBUG: USER UPDATED")
        # Check if order exists, if it does, it's fine, if not, make it
        print("DEBUG: CHECKING IF ORDER EXISTS")
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
                print("DEBUG: ORDER EXISTS, attempt:", attempt)
                break
            except Order.DoesNotExist:
                print("DEBUG: ORDER DOES NOT EXIST, attempt:", attempt)
                attempt += 1
                time.sleep(1)
                # Create the order if it does not exist
        if order_exists:
            # Create a trip instance
            if user:
                user_profile = UserProfile.objects.get(user=user)
            else:
                user_profile = None
            

            print("DEBUG: ATTEMPTING TO CREATE TRIP")
            self.create_trip(
                user,
                user_profile,
                trip_data.get('room'),
                start_date,
                end_date,
                trip_data.get('adults'),
                trip_data.get('children'),
                trip_data.get('infants'),
                grand_total
            )
            print("DEBUG: CHECK TRIP_INSTANCE IS RETURNED", trip_instance)
            
            print("DEBUG: TRIP CREATED")
            # Send confirmation email
            print("DEBUG: ATTEMPTING TO SEND EMAIL")
            self._send_confirmation_email(order, trip_instance)
            # Update room
            print("DEBUG: UPDATING ROOM")
            room_id = trip_data.get('room').id
            self.update_room(room_id, start_date, end_date)
            return HttpResponse(
                    content=(
                        f'Webhook received: {event["type"]} || '
                        f'SUCCESS: Verified order already in database'
                    ), status=200
                )
        else:
            print("ORDER DID NOT EXIST, CREATING ORDER")
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
                print("DEBUG: ORDER CREATED", order_instance)
                # Create a trip instance
                print("DEBUG: ATTEMPTING TO CREATE TRIP")
                if user:
                    user_profile = UserProfile.objects.get(user=user)
                else:
                    user_profile = None
                self.create_trip(
                    user,
                    user_profile,
                    trip_data.get('room'),
                    start_date,
                    end_date,
                    trip_data.get('adults'),
                    trip_data.get('children'),
                    trip_data.get('infants'),
                    grand_total
                )
                print("DEBUG: TRIP CREATED")
                print("DEBUG: CHECK TRIP_INSTANCE IS RETURNED", trip_instance)
            
                # Send confirmation email
                print("DEBUG: ATTEMPTING TO SEND EMAIL")
                self._send_confirmation_email(order_instance, trip_instance)
                print("DEBUG: EMAIL SENT")
                # Update room
                print("DEBUG: UPDATING ROOM")
                room_id = trip_data.get('room').id
                self.update_room(room_id, start_date, end_date)
                print("DEBUG: ROOM UPDATED")

                return HttpResponse(
                    content=(
                        f'Webhook received: {event["type"]} | '
                        f'SUCCESS: Created order in webhook'
                        ),
                    status=200)

            # If anything goes wrong, delete and 500 error
            except Exception as e:
                if order_instance:
                    order_instance.delete()
                print("DEBUG: ERROR OCCURRED:", e)
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} || ERROR: {e}',
                    status=500)

    def handle_payment_intent_payment_failed(self, event):
        '''Handle the payment_intent.payment_failed webhook event'''
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
