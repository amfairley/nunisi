from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile
from trips.models import Trip
from reviews.models import Review
from rooms.models import Amenities
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.core.paginator import Paginator
from datetime import timedelta


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
            review = Review.objects.filter(trip=trip).first()
            past_trips.append({'trip': trip, 'review': review})

    # Get amenities
    amenities = Amenities.objects.all()

    # Handle sorting
    current_sorting = 'None_None'
    sort = request.GET.get('sort')
    # If it is price_asc, order the rooms by price
    # and update current_sorting to display correctly
    if sort == 'oldest_first':
        past_trips.sort(key=lambda x: x['trip'].start_date)
        current_sorting = 'oldest_first'
    # If it is price_desc, reverse order the rooms by price
    # and update current_sorting to display correctly
    elif sort == 'newest_first':
        past_trips.sort(key=lambda x: x['trip'].start_date, reverse=True)
        current_sorting = 'newest_first'

    # Handle pagination
    page_obj = None
    paginator = Paginator(past_trips, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Include the sort value in the pagination
    def add_sort_to_url(page_num):
        return f"?page={page_num}&sort={sort}"

    context = {
        'user_profile': user_profile,
        'trips': trips,
        'upcoming_trips': upcoming_trips,
        'past_trips': past_trips,
        'amenities': amenities,
        'current-sorting': current_sorting,
        'page_obj': page_obj,
        'add_sort_to_url': add_sort_to_url,
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
        messages.error(
            request,
            "You cannot cancel a trip that has already started."
        )
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
        explanation = request.POST.get(
            'explanation',
            'No explanation provided.'
        )

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
            messages.error(
                request,
                f"An error occurred while sending the email: {e}"
            )

        return redirect('cancel_trip_success')

    messages.error(request, "Invalid request method.")
    return redirect('trips_user')


@login_required
def cancel_trip_success(request):
    """Display a success message after cancellation email is sent."""
    return render(request, 'trips/cancel_trip_success.html')


@staff_member_required
def trips_superuser(request):
    '''Display all the trips for the admin'''
    trips = Trip.objects.all().order_by('id')

    context = {
        'trips': trips,
    }
    return render(request, 'trips/trips_superuser.html', context)


def toggle_trip_status(request, trip_id):
    """Toggle the cancellation status of a trip."""
    # Check if the user is a superuser
    if not request.user.is_superuser:
        messages.error(
            request,
            "You do not have permission to perform this action."
        )
        return redirect('trips_superuser')

    # Get the trip
    trip = get_object_or_404(Trip, id=trip_id)

    # If the trip is going from not cancelled to cancelled
    if not trip.cancelled:
        remove_dates_from_room(trip)
        trip.cancelled = not trip.cancelled
        trip.save()
        status = "Cancelled" if trip.cancelled else "Confirmed"
        messages.success(request, f"Trip status updated to {status}.")
        return redirect('trips_superuser')

    # If the trip is going from cancelled to not cancelled
    elif trip.cancelled:
        if add_dates_to_room(trip) == "Conflict":
            messages.error(
                request,
                "The trip contains a room that is "
                "already booked for these dates."
            )
            return redirect('trips_superuser')
        else:
            add_dates_to_room(trip)
            trip.cancelled = not trip.cancelled
            trip.save()
            status = "Cancelled" if trip.cancelled else "Confirmed"
            messages.success(request, f"Trip status updated to {status}.")
            return redirect('trips_superuser')


def add_dates_to_room(trip):
    # Get the room
    room_booked = trip.room
    # Get the trip dates
    start_date = trip.start_date
    end_date = trip.end_date
    # Get the unavailable dates
    room_booked_unavailable_dates = room_booked.unavailability
    new_dates = []
    while start_date < end_date:
        # String the date
        date_str = start_date.strftime('%Y-%m-%d')
        # Add to new dates
        new_dates.append(date_str)
        # Increment the date by 1 day
        start_date += timedelta(days=1)
    # Check for conflicts
    print("New dates:")
    print(new_dates)
    print("Unavailable dates:")
    print(room_booked_unavailable_dates)
    for date in new_dates:
        if date in room_booked_unavailable_dates:
            return ("Conflict")
        else:
            updated_dates = room_booked_unavailable_dates + new_dates
            room_booked.unavailability = updated_dates
            room_booked.save()


def remove_dates_from_room(trip):
    # Get the room
    room_booked = trip.room
    # Get  the trip dates
    start_date = trip.start_date
    end_date = trip.end_date
    # Get the unavailable dates
    room_booked_unavailable_dates = room_booked.unavailability
    dates_to_remove = []
    while start_date < end_date:
        # String the date
        date_str = start_date.strftime('%Y-%m-%d')
        dates_to_remove.append(date_str)
        start_date += timedelta(days=1)
    updated_unavailable_dates = [
        date
        for date in room_booked_unavailable_dates
        if date not in dates_to_remove
    ]
    room_booked.unavailability = updated_unavailable_dates
    room_booked.save()
