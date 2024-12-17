from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile
from trips.models import Trip
from allauth.account.models import EmailAddress
from rooms.models import Amenities
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail


@login_required
def trips_user(request):
    ''' Display the user's trips '''
    # Get the profile from the current user
    user_profile = get_object_or_404(UserProfile, user=request.user)
    # Get the user's trips
    trips = Trip.objects.filter(profile=user_profile).order_by('start_date')
    # Split between past and upcoming trips
    today = now().date()
    upcoming_trips = []
    past_trips = []
    for trip in trips:
        if trip.start_date >= today:
            upcoming_trips.append(trip)
        else:
            past_trips.append(trip)

    # Get amenities
    amenities = Amenities.objects.all()

    context = {
        'user_profile': user_profile,
        'trips': trips,
        'upcoming_trips': upcoming_trips,
        'past_trips': past_trips,
        'amenities': amenities,
    }
    return render(request, 'trips/trips.html', context)


@login_required
def cancel_trip(request, trip_id):
    """
    Checks if the trip is eligble for cancellation.
    Error message if not.
    Directs to cancellation page if so.
    """
    # Get trip and amenities
    trip = get_object_or_404(Trip, id=trip_id, profile__user=request.user)
    amenities = Amenities.objects.all()

    # Check cancellation eligibility
    if trip.start_date < now().date():
        messages.error(request, "You cannot cancel a trip that has already started.")
        return redirect('trips_user')

    context = {
        'trip': trip,
        'amenities': amenities,
    }

    return render(request, 'trips/cancel_trip.html', context)


@login_required
def send_cancellation_email(request, trip_id):
    """
    Sends a trip cancellation request email.
    """
    # Get the trip, user and user profile for the email
    trip = get_object_or_404(Trip, id=trip_id)
    user = request.user
    user_profile = get_object_or_404(UserProfile, user=user)

    if request.method == "POST":
        explanation = request.POST.get('explanation', 'No explanation provided.')

        # Email
        recipient_email = "adamfairley1990@gmail.com"
        subject = f"Cancellation Request for Trip #{trip.id}"
        message = f"""
        Dear Team,

        The following trip cancellation has been requested:
        - Trip ID: {trip.id}
        - Check-in Date: {trip.start_date}
        - Check-out Date: {trip.end_date}
        - Room: {trip.room.sanitised_name}
        - Cost: £{trip.cost}
        - Email: {user_profile.email}
        - Explanation: {explanation}

        Please process this cancellation.
        """

        try:
            send_mail(
                subject,
                message,
                # From email
                'adamfairley1990@gmail.com',
                [recipient_email],
                fail_silently=False,
            )
            messages.success(
                request,
                "Cancellation request email sent successfully."
            )
        except Exception as e:
            messages.error(request, f"An error occurred while sending the email: {e}")

        return redirect('cancel_trip_success')

    messages.error(request, "Invalid request method.")
    return redirect('trips_user')

@login_required
def cancel_trip_success(request):
    """Display a success message after cancellation email is sent."""
    return render(request, 'trips/cancel_trip_success.html')