from django.test import TestCase
from .forms import BookingForm


class BookingFormTest(TestCase):
    def booking_form_exists(self):
        form = BookingForm()
        self.assertIsInstance(form, BookingForm)
