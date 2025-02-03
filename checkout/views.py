from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.http import require_POST
from django.conf import settings
from django.contrib import messages
from rooms.models import Room
from user_profile.models import UserProfile
from django.contrib.auth.models import User
from .forms import CheckoutForm
from .models import Order
import stripe
from datetime import datetime
import json


@require_POST
def cache_checkout_data(request):
    '''
    Before calling confirm payment in JS
    Make a post request to this view and give it the client secret
    From the payment intent
    '''
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY

        user_email = None
        if request.user.is_authenticated:
            user_email = request.user.email
            save_info = request.POST.get('save_info')
        else:
            user_email = request.POST.get('email')
            print(user_email)
            save_info = False

        stripe.PaymentIntent.modify(
            pid,
            metadata={
                'trip_data': json.dumps({
                    'room': request.POST.get('room_id'),
                    'start_date': request.POST.get('check_in_date'),
                    'end_date': request.POST.get('check_out_date'),
                    'adults': request.POST.get('adults'),
                    'children': request.POST.get('children'),
                    'infants': request.POST.get('infants'),
                    'cost': request.POST.get('total_cost'),
                }),
                'save_info': save_info,
                'user_email': user_email,
            }
        )
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(
            request,
            'Sorry, your payment cannot be processed right now. '
            'Please try again later.'
        )
        return HttpResponse(content=e, status=400)


def checkout(request):
    '''A view to return the checkout'''
    # Initialise variables
    room_id = None
    total_days = None
    check_in_date = None
    sanitised_check_in_date = None
    check_out_date = None
    sanitised_check_out_date = None
    total_guests = None
    adults = None
    children = None
    infants = None
    room = None
    total_cost = None
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    intent = None
    client_secret = None
    checkout_form = CheckoutForm()

    # Base context
    context = {
        'checkout_form': checkout_form,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'client_secret': None,
    }

    if request.POST:
        if 'direct_to_checkout' in request.POST:
            # Get values from the form
            room_id = request.POST.get('room_id')
            total_days = request.POST.get('total_days')
            check_in_date = request.POST.get('check_in_date')
            check_out_date = request.POST.get('check_out_date')
            # Sanitise data data
            check_in_date_object = datetime.strptime(check_in_date, '%Y-%m-%d')
            sanitised_check_in_date = check_in_date_object.strftime('%d-%b-%Y')
            check_out_date_object = datetime.strptime(
                check_out_date,
                '%Y-%m-%d'
            )
            sanitised_check_out_date = check_out_date_object.strftime(
                '%d-%b-%Y'
            )
            # Guest data
            adults = request.POST.get('adults')
            if request.POST.get('children') == '':
                children = 0
            else:
                children = request.POST.get('children')
            if request.POST.get('infants') == '':
                infants = 0
            else:
                infants = request.POST.get('infants')
            total_guests = int(adults) + int(children) + int(infants)
            room = Room.objects.get(id=room_id)
            cost_per_night = room.price
            total_cost = cost_per_night * int(total_days)

            # Create a payment intent
            # stripe requires total to be an integer
            stripe_total = int(round(total_cost * 100))
            stripe.api_key = stripe_secret_key



            # intent = stripe.PaymentIntent.create(
            #     amount=stripe_total,
            #     currency=settings.STRIPE_CURRENCY,
            # )

            try:
                intent = stripe.PaymentIntent.create(
                    amount=stripe_total,
                    currency=settings.STRIPE_CURRENCY,
                )
                client_secret = intent['client_secret']
            except stripe.error.CardError as e:
                messages.error(
                    request,
                    f"Payment failed: {e.user_message}. Please try again."
                )
                return redirect('checkout') 


            client_secret = intent['client_secret']
            # Helpful message to display if the public key has not been set
            if not stripe_public_key:
                messages.warning(request, 'Stripe public key is missing. \
                    Did you forget to set it in your environment?')

            # Prefill the checkout form
            if request.user.is_authenticated:
                try:
                    user_profile = UserProfile.objects.get(user=request.user)
                    checkout_form = CheckoutForm(initial={
                        'full_name': user_profile.full_name,
                        'email': user_profile.user.email,
                        'phone_number': user_profile.phone_number,
                        'street_address1': user_profile.street_address1,
                        'street_address2': user_profile.street_address2,
                        'town_or_city': user_profile.town_or_city,
                        'county': user_profile.county,
                        'postcode': user_profile.postcode,
                        'country': user_profile.country,
                    })
                except UserProfile.DoesNotExist:
                    checkout_form = CheckoutForm()

            context.update({
                'room_id': room_id,
                'room': room,
                'total_days': total_days,
                'check_in_date': check_in_date,
                'sanitised_check_in_date': sanitised_check_in_date,
                'check_out_date': check_out_date,
                'sanitised_check_out_date': sanitised_check_out_date,
                'total_guests': total_guests,
                'adults': adults,
                'children': children,
                'infants': infants,
                'total_cost': total_cost,
                'client_secret': client_secret,
                'checkout_form': checkout_form,
            })
            return render(request, 'checkout/checkout.html', context)

        elif 'payment_form' in request.POST:
            stripe_secret_key = settings.STRIPE_SECRET_KEY
            stripe_public_key = settings.STRIPE_PUBLIC_KEY
            # Get save info status
            save_info = request.POST.get('save_info')
            # Set form values as a dictionary
            if request.user.is_authenticated:
                try:
                    user_profile_submit = UserProfile.objects.get(
                        user=request.user
                    )
                except UserProfile.DoesNotExist:
                    user_profile_submit = None
            else:
                user_profile_submit = None
            order_form_data = {
                'user_profile': user_profile_submit,
                'full_name': request.POST.get('full_name'),
                'email': request.POST.get('email'),
                'phone_number': request.POST.get('phone_number'),
                'country': request.POST.get('country'),
                'postcode': request.POST.get('postcode'),
                'town_or_city': request.POST.get('town_or_city'),
                'street_address1': request.POST.get('street_address1'),
                'street_address2': request.POST.get('street_address2'),
                'county': request.POST.get('county'),
                'order_total': float(request.POST.get('total_cost')),
                'stripe_pid': request.POST.get('client_secret'),
            }

            # If the save info button is ticked:
            if save_info:
                # Get the user profile
                user_profile = UserProfile.objects.get(user=request.user)
                # Update the user profile with the form data
                user_profile.full_name = order_form_data['full_name']
                user_profile.phone_number = order_form_data['phone_number']
                user_profile.country = order_form_data['country']
                user_profile.postcode = order_form_data['postcode']
                user_profile.town_or_city = order_form_data['town_or_city']
                user_profile.street_address1 = order_form_data[
                    'street_address1'
                ]
                user_profile.street_address2 = order_form_data[
                    'street_address2'
                ]
                user_profile.county = order_form_data['county']
                user_profile.save()

            # Create an order instance
            order_instance = Order(**order_form_data)
            order_instance.save()
            order_instance.__str__()

            print(intent)
            # Helpful message to display if the public key has not been set
            if not stripe_public_key:
                messages.warning(request, 'Stripe public key is missing. \
                    Did you forget to set it in your environment?')

            context.update({
                'client_secret': client_secret,
                'order': order_instance,
            })

            return render(request, 'checkout/success.html', context)
    return (render(request, 'checkout/checkout.html', context))
