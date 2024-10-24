from .forms import BookingForm


def booking_form(request):
    '''Add the booking form to the context'''
    return {
        'booking_form': BookingForm()
    }
