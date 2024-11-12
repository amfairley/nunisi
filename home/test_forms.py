from django.test import TestCase
from .forms import BookingForm
from datetime import date, timedelta


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
            '<label for="id_check_in_date">Check-in:</label>'
        )

    def test_check_out_required(self):
        '''Tests that the check out section is required'''
        form = BookingForm({'check_out_date': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('check_out_date', form.errors)

    def test_check_out_label(self):
        '''Tests the check out label'''
        form = BookingForm()
        form_label = form['check_out_date'].label_tag()
        self.assertEqual(
            form_label,
            '<label for="id_check_out_date">Check-out:</label>'
        )

    def test_adults_required(self):
        '''Tests that the adults selection is required'''
        form = BookingForm({'adults': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('adults', form.errors)

    def test_adults_label(self):
        '''Tests the adults label'''
        form = BookingForm()
        form_label = form['adults'].label_tag()
        self.assertEqual(
            form_label,
            '<label for="id_adults">Adults (18+):</label>'
        )

    def test_adults_values(self):
        '''Tests that valid values for adults is 1-5'''
        form = BookingForm({
            'check_in_date': '2025-08-10',
            'check_out_date': '2025-08-11',
            'adults': 0,
            'children': 1,
            'infants': 1
        })
        self.assertFalse(form.is_valid())
        form = BookingForm({
            'check_in_date': '2025-08-10',
            'check_out_date': '2025-08-11',
            'adults': 1,
            'children': 1,
            'infants': 1
        })
        self.assertTrue(form.is_valid())
        form = BookingForm({
            'check_in_date': '2025-08-10',
            'check_out_date': '2025-08-11',
            'adults': 5,
            'children': 1,
            'infants': 1
        })
        self.assertTrue(form.is_valid())
        form = BookingForm({
            'check_in_date': '2025-08-10',
            'check_out_date': '2025-08-11',
            'adults': 6,
            'children': 1,
            'infants': 1
        })
        self.assertFalse(form.is_valid())

    def test_children_required(self):
        '''Tests that the children selection is required'''
        form = BookingForm({'children': ''})
        self.assertNotIn('children', form.errors)

    def test_children_label(self):
        '''Tests the children label'''
        form = BookingForm()
        form_label = form['children'].label_tag()
        self.assertEqual(
            form_label,
            '<label for="id_children">Children (5+):</label>'
        )

    def test_children_values(self):
        '''Tests that valid values for children is 1-5'''
        form = BookingForm({
            'check_in_date': '2025-08-10',
            'check_out_date': '2025-08-11',
            'adults': 1,
            'children': -1,
            'infants': 1
        })
        self.assertFalse(form.is_valid())
        form = BookingForm({
            'check_in_date': '2025-08-10',
            'check_out_date': '2025-08-11',
            'adults': 1,
            'children': 0,
            'infants': 1
        })
        self.assertTrue(form.is_valid())
        form = BookingForm({
            'check_in_date': '2025-08-10',
            'check_out_date': '2025-08-11',
            'adults': 1,
            'children': 5,
            'infants': 1
        })
        self.assertTrue(form.is_valid())
        form = BookingForm({
            'check_in_date': '2025-08-10',
            'check_out_date': '2025-08-11',
            'adults': 1,
            'children': 6,
            'infants': 1
        })
        self.assertFalse(form.is_valid())

    def test_infants_required(self):
        '''Tests that the infants selection is required'''
        form = BookingForm({'infants': ''})
        self.assertNotIn('infants', form.errors)

    def test_infants_label(self):
        '''Tests the infants label'''
        form = BookingForm()
        form_label = form['infants'].label_tag()
        self.assertEqual(
            form_label,
            '<label for="id_infants">Infants (0-5):</label>'
        )

    def test_infants_values(self):
        '''Tests that valid values for infants is 1-5'''
        form = BookingForm({
            'check_in_date': '2025-08-10',
            'check_out_date': '2025-08-11',
            'adults': 1,
            'children': 1,
            'infants': -1
        })
        self.assertFalse(form.is_valid())
        form = BookingForm({
            'check_in_date': '2025-08-10',
            'check_out_date': '2025-08-11',
            'adults': 1,
            'children': 1,
            'infants': 0
        })
        self.assertTrue(form.is_valid())
        form = BookingForm({
            'check_in_date': '2025-08-10',
            'check_out_date': '2025-08-11',
            'adults': 1,
            'children': 1,
            'infants': 5
        })
        self.assertTrue(form.is_valid())
        form = BookingForm({
            'check_in_date': '2025-08-10',
            'check_out_date': '2025-08-11',
            'adults': 1,
            'children': 1,
            'infants': 6
        })
        self.assertFalse(form.is_valid())

    def test_booking_meta_fields(self):
        form = BookingForm()
        self.assertEqual(
            form.Meta.fields,
            [
                'check_in_date',
                'check_out_date',
                'adults',
                'children',
                'infants'
            ]
        )

    def test_check_in_date_minimum(self):
        """Tests that the check-in date must be tomorrow or later"""
        # Set the date to today
        form = BookingForm({
            'check_in_date': date.today().isoformat(),
            # Set check out in 2 days
            'check_out_date': (date.today() + timedelta(days=2)).isoformat(),
            'adults': 1,
        })
        # Check if the form is invalid
        self.assertFalse(form.is_valid())
        self.assertIn('check_in_date', form.errors)

        # Test with tomorrow (valid)
        form = BookingForm({
            'check_in_date': (date.today() + timedelta(days=1)).isoformat(),
            'check_out_date': (date.today() + timedelta(days=2)).isoformat(),
            'adults': 1,
        })
        self.assertTrue(form.is_valid())

    def test_check_out_date_after_check_in(self):
        """Tests that the check-out date must be after the check-in date"""
        # Test check out date before check in date
        form = BookingForm({
            'check_in_date': (date.today() + timedelta(days=1)).isoformat(),
            'check_out_date': date.today().isoformat(),
            'adults': 1,
        })
        # Test that this is invalid
        self.assertFalse(form.is_valid())
        self.assertIn('check_out_date', form.errors)

        # Test check out date after check in date
        form = BookingForm({
            'check_in_date': (date.today() + timedelta(days=1)).isoformat(),
            'check_out_date': (date.today() + timedelta(days=2)).isoformat(),
            'adults': 1,
        })
        self.assertTrue(form.is_valid())
