from django.shortcuts import render, get_object_or_404, redirect
from .models import Room, Amenities
from .forms import EditRoomForm
from home.forms import BookingForm
from datetime import timedelta
from django.contrib.admin.views.decorators import staff_member_required


def available_rooms(request):
    '''Search and filter rooms to find available rooms'''
    rooms = Room.objects.all()
    amenities = Amenities.objects.all()
    trip_dates = []
    valid_rooms = []
    total_days = 0

    # Initialize booking forms
    booking_form_mobile = BookingForm(prefix="mobile")
    booking_form_desktop = BookingForm(prefix="desktop")
    booking_form = None

    if request.POST:
        # Define the mobile and desktop instances
        booking_form_mobile = BookingForm(
            request.POST or None,
            prefix="mobile"
        )
        booking_form_desktop = BookingForm(
            request.POST or None, prefix="desktop"
        )

        # Asign the booking form
        booking_form = None
        if 'mobile-check_in_date' in request.POST:
            booking_form = booking_form_mobile
        elif 'desktop-check_in_date' in request.POST:
            booking_form = booking_form_desktop

        # Check that the form is not None and it is valid
        if booking_form and booking_form.is_valid():
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
            # Get total guests
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
                'amenities': amenities,
                # Booking form for iterating through errors
                'booking_form': booking_form,
                # Booking form desktop for populating header form
                'booking_form_desktop': booking_form_desktop,
                'check_in_date': check_in_date,
                'check_out_date': check_out_date,
                'adults': adults,
                'children': children,
                'infants': infants,
                'total_guests': total_guests,
                'trip_dates': trip_dates,
                'total_days': total_days,
                'total_cost': total_cost,
                'valid_rooms': valid_rooms,
            }

            return render(request, 'rooms/available_rooms.html', context)

    context = {
        # Booking form for iterating through errors
        'booking_form': booking_form,
        # Booking form desktop for populating header form
        'booking_form_desktop': booking_form_desktop,
        'rooms': rooms,
        'amenities': amenities,
        'valid_rooms': valid_rooms,
    }
    return render(request, 'rooms/available_rooms.html', context)


@staff_member_required
def rooms_superuser(request):
    '''Display all the rooms for the admin to view/edit/delete'''
    rooms = Room.objects.all()
    amenities = Amenities.objects.all()

    context = {
        'rooms': rooms,
        'amenities': amenities,
    }
    return render(request, 'rooms/rooms_superuser.html', context)


@staff_member_required
def edit_room(request, room_id):
    """Display and handle the room edit form for admins."""
    # Get the room
    room = get_object_or_404(Room, id=room_id)
    amenities = amenities = Amenities.objects.all().order_by('id')
    # If the form is submitted
    if request.method == 'POST':
        # request.FILES handles the image upload
        form = EditRoomForm(request.POST, request.FILES, instance=room)
        if form.is_valid():
            form.save()
            # Redirect to rooms_superuser view or another page after saving
            return redirect('rooms_superuser')
    else:
        form = EditRoomForm(instance=room)

    context = {
        'form': form,
        'room': room,
        'amenities': amenities,
    }
    return render(request, 'rooms/edit_room.html', context)


@staff_member_required
def delete_room(request, room_id):
    """Delete a room from the database."""
    room = get_object_or_404(Room, id=room_id)

    # Delete confirmation
    if request.method == 'POST':
        room.delete()
        return redirect('rooms_superuser')

    context = {
        'room': room
    }
    return render(request, 'rooms/delete_room.html', context)


@staff_member_required
def add_room(request):
    '''View to enter details and add a new room'''
    amenities = Amenities.objects.all().order_by('id')
    form = EditRoomForm()

    # If the form is submitted
    if request.method == 'POST':
        # request.FILES handles the image upload
        form = EditRoomForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirect to rooms_superuser view or another page after saving
            return redirect('rooms_superuser')

    context = {
        'form': form,
        'amenities': amenities,
    }
    return render(request, 'rooms/add_room.html', context)
