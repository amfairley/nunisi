from django.shortcuts import render
from .models import Room, Amenities
from home.forms import BookingForm
from datetime import timedelta


def available_rooms(request):
    '''Search and filter rooms to find available rooms'''
    rooms = Room.objects.all()
    amenities = Amenities.objects.all()
    trip_dates = []
    valid_rooms = []
    total_days = 0

    if request.GET:
        booking_form = BookingForm(request.GET or None)

        if booking_form.is_valid():
            # Get user input data
            check_in_date = booking_form.cleaned_data['check_in_date']
            check_out_date = booking_form.cleaned_data['check_out_date']
            adults = booking_form.cleaned_data['adults']
            # Put in 0 for no value entered for children
            if not booking_form.cleaned_data['children']:
                children = 0
            else:
                children = booking_form.cleaned_data['children']
            # Put in 0 for no value entered for infants
            if not booking_form.cleaned_data['infants']:
                infants = 0
            else:
                infants = booking_form.cleaned_data['infants']
            total_guests = int(adults) + int(children) + int(infants)

            # Get a list of all dates for the trip
            current_date = check_in_date

            while current_date <= check_out_date:
                trip_dates.append(current_date)
                current_date += timedelta(days=1)

            # Get the length of the trip
            total_days = (check_out_date - check_in_date).days

            # Find suitable rooms
            for room in rooms:
                # Check if any trip_dates are in the room's unavailability list
                if any(date in room.unavailability for date in trip_dates):
                    continue

                # Calculate amount of people the room sleeps based on amenities
                sleeps = 0
                for amenity in room.amenities:
                    if amenity == 1:
                        sleeps += 1
                    elif amenity == 2:
                        sleeps += 2

                # Get the total cost of the room
                total_cost = total_days * room.price

                # Check if the room can accommodate the total guests
                if sleeps >= total_guests:
                    valid_rooms.append({
                        'room': room,
                        'total_cost': total_cost,
                    })

    context = {
        'rooms': rooms,
        'booking_form': booking_form,
        'trip_dates': trip_dates,
        'valid_rooms': valid_rooms,
        'amenities': amenities,
        'total_days': total_days,
    }

    return render(request, 'rooms/available_rooms.html', context)
