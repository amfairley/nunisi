from django.test import TestCase
from .forms import BookingForm


class BookingFormTest(TestCase):
    '''Tests for the booking form'''
    def test_booking_form_exists(self):
        '''Tests that the booking form exists and is defined'''
        form = BookingForm()
        self.assertIsInstance(form, BookingForm)

    def test_name_form_required(self):
        '''Tests that the name form is required'''
        form = BookingForm({'check_in_date': ''})
        self.assertTrue(form.is_valid())
