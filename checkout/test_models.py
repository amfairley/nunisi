from django.test import TestCase
from django.apps import apps
from .models import Order
from django.db.models import (
    CharField
)


class RoomModelTest(TestCase):
    '''Tests for the Room model'''
    def test_model_exists(self):
        '''Check that the app is installed and model defined'''
        self.assertTrue(apps.is_installed('checkout'))
        self.assertIn(
            'Order', [model.__name__ for model in apps.get_models()]
        )

    def test_order_number_field(self):
        '''Test the order number field'''
        # Get the 'order_number' field from the model
        field = Order._meta.get_field('order_number')
        # Check that the field is a CharField
        self.assertIsInstance(field, CharField)
        self.assertEqual(field.get_internal_type(), 'CharField')
        # Check the max length of the CharField
        self.assertEqual(field.max_length, 32)
        # Check null status
        self.assertFalse(field.null)
        # Check blank status
        self.assertFalse(field.editable)
