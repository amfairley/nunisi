from django.http import HttpResponse
from .models import Order
from user_profile.models import UserProfile
import stripe
import time


class StripeWH_Handler:
    '''Handle Stripe Webhooks'''

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        '''Handle a generic/unknown/unexpected webhook event'''
        return HttpResponse(
            content=f'Unhandled Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        '''Handle the payment_intent.succeeded webhook event'''
        intent = event.data.object
        pid = intent.id
        trip_data = intent.metadata.trip_data
        save_info = intent.metadata.save_info

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
        user_profile = None
        user = intent.metadata.user
        if user.is_authenticated:
            user_profile = UserProfile.objects.get(user=user)
            if save_info:
                user_profile.full_name = shipping_details.name
                user_profile.phone_number = shipping_details.phone
                user_profile.country = shipping_details.address.country
                user_profile.postcode = shipping_details.address.postal_code
                user_profile.town_or_city = shipping_details.address.city
                user_profile.street_address1 = shipping_details.address.line1
                user_profile.street_address2 = shipping_details.address.line2
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
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
                # Create the order if it does not exist
        if order_exists:
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
        print(intent)
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
