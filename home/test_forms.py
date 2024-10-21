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

    def test_check_in_label(self):
        '''Tests the check in label'''
        form = BookingForm()
        form_label = form['check_in_date'].label_tag()
        self.assertEqual(
            form_label,
            '<label for="id_check_in_date">Check-in date:</label>'
        )

    def test_check_out_required(self):
        '''Tests that the check out section is required'''
        form = BookingForm({'check_out_date': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('check_out_date', form.errors)
