from .forms import BookingForm


def booking_form(request):
    '''Add the booking form to the context'''
    return {
        'booking_form_mobile': BookingForm(prefix="mobile"),
        'booking_form_desktop': BookingForm(prefix="desktop"),
    }
