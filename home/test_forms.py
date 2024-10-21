from django.test import TestCase
from .forms import BookingForm


class BookingFormTest(TestCase):
    '''Tests for the booking form'''
    def test_booking_form_exists(self):
        '''Tests that the booking form exists and is defined'''
        form = BookingForm()
        self.assertIsInstance(form, BookingForm)

    def test_check_in_required(self):
        '''Tests that the check in section is required'''
        form = BookingForm({'check_in_date': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('check_in_date', form.errors)

    def test_check_in_widget(self):
        '''Tests correct check in widget'''
        form = BookingForm()
        self.assertEqual(
            form.fields['check_in_date'].widget.attrs['type'],
            'date'
        )
