from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
from rooms.models import Room
import stripe


# Initialize Stripe keys


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
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    stripe_public_key = settings.STRIPE_PUBLIC_KEY

    if request.POST:
        # Get values from the form
        room_id = request.POST.get('room_id')
        total_days = request.POST.get('total_days')
        check_in_date = request.POST.get('check_in_date')
        check_out_date = request.POST.get('check_out_date')
        adults = request.POST.get('adults')
        children = request.POST.get('children')
        infants = request.POST.get('infants')
        room = Room.objects.get(id=room_id)
        cost_per_night = room.price
        total_cost = cost_per_night * int(total_days)
        # stripe requires total to be an integer
        stripe_total = int(total_cost * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
    print(intent)

    # Helpful message to display if the public key has not been set
    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    context = {
        'room_id': room_id,
        'total_days': total_days,
        'check_in_date': check_in_date,
        'check_out_date': check_out_date,
        'adults': adults,
        'children': children,
        'infants': infants,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    return render(request, 'checkout/checkout.html', context)
