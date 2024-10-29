from django.test import TestCase
from django.apps import apps
from django.db.models import CharField, JSONField
from .models import Room


class RoomModelTest(TestCase):
    '''Tests for the Room model'''
    def setUp(self):
        '''Creates an instance of the model to test'''
        self.instance = Room.objects.create(
            name="Test Name",
            sanitised_name="Sanitised Test Name",
            amenities=[1, 2, 3]
        )

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
    
    def test_sanitised_name_field(self):
        '''Test the sanitised name field'''
        # Get the 'sanitised_name' field from the model
        field = Room._meta.get_field('sanitised_name')
        # Check the field is a Charfield
        self.assertIsInstance(field, CharField)
        # Check the max length of the CharField
        self.assertEqual(field.max_length, 254)
        # Check null status
        self.assertFalse(field.null)
        # Check blank status
        self.assertFalse(field.blank)

    def test_amenities_field(self):
        '''Test the amenities field'''
        # Get the 'amenities' field from the model
        field = Room._meta.get_field('amenities')
        # Check the field is a JSONField
        self.assertIsInstance(field, JSONField)
        # Check the JSONField default
        self.assertEqual(self.instance.amenities, [1, 2, 3])
        # Check null status
        self.assertFalse(field.null)
        # Check blank status
        self.assertFalse(field.blank)

