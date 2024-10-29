from django.test import TestCase
from django.apps import apps
from django.db.models import CharField
from .models import Room


class RoomModelTest(TestCase):
    '''Tests for the Room model'''
    def test_room_model_exists(self):
        '''Check that the app is installed and model defined'''
        self.assertTrue(apps.is_installed('rooms'))
        self.assertIn(
            'Room', [model.__name__ for model in apps.get_models()]
        )

    def test_name_field(self):
        '''Test the name field'''
        # Get the 'name' field from the model
        field = Room._meta.get_field('name')
        # Check that the field is a CharField
        self.assertIsInstance(field, CharField)
        self.assertEqual(field.get_internal_type(), 'CharField')
        # Check the max length of the CharField
        self.assertEqual(field.max_length, 254)
        # Check null status
        self.assertFalse(field.null)
        # Check blank status
        self.assertFalse(field.blank)
