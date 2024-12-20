from django.test import TestCase
from .models import Trip
from django.apps import apps
from django.db.models import (
    BooleanField,
    ForeignKey,
    DateField,
    IntegerField,
    DecimalField,
)


class TripModelTest(TestCase):
    '''Test the Trip model'''
    def test_trip_model_exists(self):
        '''Check that the app is installed and model defined'''
        self.assertTrue(apps.is_installed('trips'))
        self.assertIn(
            'Trip', [model.__name__ for model in apps.get_models()]
        )

    def test_profile_field(self):
        '''Test the profile field'''
        # Get the 'profile' field from the model
        field = Trip._meta.get_field('profile')
        # Check that the field is a ForeignKey
        self.assertIsInstance(field, ForeignKey)
        self.assertEqual(field.get_internal_type(), 'ForeignKey')
        # Check null status
        self.assertTrue(field.null)
        # Check blank status
        self.assertTrue(field.blank)

    def test_room_field(self):
        '''Test the room field'''
        # Get the 'room' field from the model
        field = Trip._meta.get_field('room')
        # Check that the field is a ForeignKey
        self.assertIsInstance(field, ForeignKey)
        self.assertEqual(field.get_internal_type(), 'ForeignKey')
        # Check null status
        self.assertTrue(field.null)
        # Check blank status
        self.assertTrue(field.blank)

    def test_start_date_field(self):
        '''Test the start_date field'''
        # Get the 'start_date' field from the model
        field = Trip._meta.get_field('start_date')
        # Check that the field is a DateField
        self.assertIsInstance(field, DateField)
        self.assertEqual(field.get_internal_type(), 'DateField')
        # Check null status
        self.assertFalse(field.null)
        # Check blank status
        self.assertFalse(field.blank)

    def test_end_date_field(self):
        '''Test the end_date field'''
        # Get the 'end_date' field from the model
        field = Trip._meta.get_field('end_date')
        # Check that the field is a DateField
        self.assertIsInstance(field, DateField)
        self.assertEqual(field.get_internal_type(), 'DateField')
        # Check null status
        self.assertFalse(field.null)
        # Check blank status
        self.assertFalse(field.blank)

    def test_adults_field(self):
        '''Test the adults field'''
        # Get the 'adults' field from the model
        field = Trip._meta.get_field('adults')
        # Check that the field is a IntegerField
        self.assertIsInstance(field, IntegerField)
        self.assertEqual(field.get_internal_type(), 'IntegerField')
        # Check null status
        self.assertFalse(field.null)
        # Check blank status
        self.assertFalse(field.blank)

    def test_children_field(self):
        '''Test the children field'''
        # Get the 'children' field from the model
        field = Trip._meta.get_field('children')
        # Check that the field is a IntegerField
        self.assertIsInstance(field, IntegerField)
        self.assertEqual(field.get_internal_type(), 'IntegerField')
        # Check default
        self.assertEqual(field.default, 0)

    def test_infants_field(self):
        '''Test the infants field'''
        # Get the 'infants' field from the model
        field = Trip._meta.get_field('infants')
        # Check that the field is a IntegerField
        self.assertIsInstance(field, IntegerField)
        self.assertEqual(field.get_internal_type(), 'IntegerField')
        # Check default
        self.assertEqual(field.default, 0)

    def test_cost_field(self):
        '''Test the cost field'''
        # Get the 'cost' field from the model
        field = Trip._meta.get_field('cost')
        # Check that the field is a DecimalField
        self.assertIsInstance(field, DecimalField)
        self.assertEqual(field.get_internal_type(), 'DecimalField')
        # Check null status
        self.assertFalse(field.null)
        # Check max digits
        self.assertEqual(field.max_digits, 10)
        # Check decimal places
        self.assertEqual(field.decimal_places, 2)

    def test_cancelled_field(self):
        '''Test the cancelled field'''
        # Get the 'cancelled' field from the model
        field = Trip._meta.get_field('cancelled')
        # Check that the field is a BooleanField
        self.assertIsInstance(field, BooleanField)
        self.assertEqual(field.get_internal_type(), 'BooleanField')
        # Check default
        self.assertEqual(field.default, False)
