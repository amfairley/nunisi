from django.shortcuts import render, HttpResponse
from django.views.decorators.http import require_POST
from django.conf import settings
from django.contrib import messages
from rooms.models import Room
from .forms import CheckoutForm
from .models import Order
import stripe


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
        stripe.PaymentIntent.modify(pid, metadata={
            'trip_data': {
                'room': request.POST.get('room_id'),
                'start_date': request.POST.get('check_in_date'),
                'end_date': request.POST.get('check_out_date'),
                'adults': request.POST.get('adults'),
                'children': request.POST.get('children'),
                'infants': request.POST.get('infants'),
            },
            
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
                       processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    '''A view to return the checkout'''
    # Initialise variables
    room_id = None
    total_days = None
    check_in_date = None
    check_out_date = None
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

    if request.POST:
        if 'direct_to_checkout' in request.POST:
            # Get values from the form
            room_id = request.POST.get('room_id')
            total_days = request.POST.get('total_days')
            check_in_date = request.POST.get('check_in_date')
            check_out_date = request.POST.get('check_out_date')
            adults = request.POST.get('adults')
            if request.POST.get('children') == '':
                children = 0
            else:
                children = request.POST.get('children')
            if request.POST.get('infants') == '':
                infants = 0
            else:
                infants = request.POST.get('infants')
            room = Room.objects.get(id=room_id)
            cost_per_night = room.price
            total_cost = cost_per_night * int(total_days)

            # Create a payment intent
            # stripe requires total to be an integer
            stripe_total = int(round(total_cost * 100))
            stripe.api_key = stripe_secret_key
            intent = stripe.PaymentIntent.create(
                amount=stripe_total,
                currency=settings.STRIPE_CURRENCY,

            )
            client_secret = intent.client_secret
            # Helpful message to display if the public key has not been set
            if not stripe_public_key:
                messages.warning(request, 'Stripe public key is missing. \
                    Did you forget to set it in your environment?')

            context = {
                'room_id': room_id,
                'room': room,
                'total_days': total_days,
                'check_in_date': check_in_date,
                'check_out_date': check_out_date,
                'adults': adults,
                'children': children,
                'infants': infants,
                'total_cost': total_cost,
                'checkout_form': checkout_form,
                'stripe_public_key': stripe_public_key,
                'client_secret': client_secret,
            }
            return render(request, 'checkout/checkout.html', context)

        elif 'payment_form' in request.POST:
            stripe_secret_key = settings.STRIPE_SECRET_KEY
            stripe_public_key = settings.STRIPE_PUBLIC_KEY
            # Set form values as a dictionary
            order_form_data = {
                'full_name': request.POST.get('full_name'),
                'email': request.POST.get('email'),
                'phone_number': request.POST.get('phone_number'),
                'country': request.POST.get('country'),
                'postcode': request.POST.get('postcode'),
                'town_or_city': request.POST.get('town_or_city'),
                'street_address1': request.POST.get('street_address1'),
                'street_address2': request.POST.get('street_address2'),
                'county': request.POST.get('county'),
                'order_total': float(request.POST.get('total_cost'))
            }

            # Create an order instance
            order_instance = Order(**order_form_data)
            order_instance.save()
            order_instance.__str__()

            print(intent)
            # Helpful message to display if the public key has not been set
            if not stripe_public_key:
                messages.warning(request, 'Stripe public key is missing. \
                    Did you forget to set it in your environment?')

            context = {
                'stripe_public_key': stripe_public_key,
                'client_secret': client_secret,
                'order_number': order_instance.order_number,
            }

            return render(request, 'checkout/success.html', context)
    return (render(request, 'checkout/checkout.html', context))
