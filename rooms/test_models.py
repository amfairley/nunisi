from django.test import TestCase
from django.apps import apps
from django.db.models import (
    CharField,
    JSONField,
    TextField,
    URLField,
    ImageField,
    DecimalField
)
from .models import Room, Amenities


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

    def test_description_field(self):
        '''Test the description field'''
        # Get the 'description' field from the model
        field = Room._meta.get_field('description')
        # Check the field is a TextField
        self.assertIsInstance(field, TextField)
        # Check the TextField default
        self.assertEqual(self.instance.description, 'Room Description')
        # Check null status
        self.assertFalse(field.null)
        # Check blank status
        self.assertFalse(field.blank)

    def test_image_url_field(self):
        '''Test the image_url field'''
        # Get the 'image_url' field from the model
        field = Room._meta.get_field('image_url')
        # Check the field is a URLField
        self.assertIsInstance(field, URLField)
        # Check null status
        self.assertTrue(field.null)
        # Check blank status
        self.assertTrue(field.blank)

    def test_image_field(self):
        '''Test the image field'''
        # Get the 'image' field from the model
        field = Room._meta.get_field('image')
        # Check the field is a URLField
        self.assertIsInstance(field, ImageField)
        # Check null status
        self.assertTrue(field.null)
        # Check blank status
        self.assertTrue(field.blank)

    def test_price_field(self):
        '''Test the price field'''
        # Get the 'price' field from the model
        field = Room._meta.get_field('price')
        # Check the field is a DecimalField
        self.assertIsInstance(field, DecimalField)
        # Check null status
        self.assertTrue(field.null)
        # Check blank status
        self.assertTrue(field.blank)

    def test_unavailability_field(self):
        '''Test the unavailability field'''
        # Get the 'unavailability' field from the model
        field = Room._meta.get_field('unavailability')
        # Check the field is a JSONField
        self.assertIsInstance(field, JSONField)
        # Check the JSONField default
        self.assertEqual(self.instance.unavailability, [])
        # Check null status
        self.assertFalse(field.null)
        # Check blank status
        self.assertTrue(field.blank)

    def test_str_method(self):
        '''Test the string method'''
        self.assertEqual(str(self.instance), "Test Name")

    def test_get_sanitised_name_method(self):
        '''Test the get_sanitised_name method'''
        self.assertEqual(
            self.instance.get_sanitised_name(),
            "Sanitised Test Name"
        )


class AmenitiesModelTest(TestCase):
    '''Tests for the Amenities model'''
    def setUp(self):
        '''Creates an instance of the model to test'''
        self.instance = Amenities.objects.create(
            name="Test Name"
        )

    def test_amenities_model_exists(self):
        '''Check that the app is installed and model defined'''
        self.assertTrue(apps.is_installed('rooms'))
        self.assertIn(
            'Amenities', [model.__name__ for model in apps.get_models()]
        )

    def test_name_field(self):
        '''Test the name field'''
        # Get the 'name' field from the model
        field = Amenities._meta.get_field('name')
        # Check that the field is a CharField
        self.assertIsInstance(field, CharField)
        self.assertEqual(field.get_internal_type(), 'CharField')
        # Check the max length of the CharField
        self.assertEqual(field.max_length, 50)
        # Check null status
        self.assertFalse(field.null)
        # Check blank status
        self.assertFalse(field.blank)

    def test_sanitised_name_field(self):
        '''Test the sanitised name field'''
        # Get the 'sanitised_name' field from the model
        field = Amenities._meta.get_field('sanitised_name')
        # Check the field is a Charfield
        self.assertIsInstance(field, CharField)
        # Check the max length of the CharField
        self.assertEqual(field.max_length, 100)
        # Check null status
        self.assertFalse(field.null)
        # Check blank status
        self.assertFalse(field.blank)
        # Check default value
        self.assertEqual(self.instance.sanitised_name, "Amenity Name")

    def test_icon_field(self):
        '''Test the icon name field'''
        # Get the 'icon' field from the model
        field = Amenities._meta.get_field('icon')
        # Check the field is a Charfield
        self.assertIsInstance(field, CharField)
        # Check the max length of the CharField
        self.assertEqual(field.max_length, 150)
        # Check null status
        self.assertFalse(field.null)
        # Check blank status
        self.assertFalse(field.blank)
        # Check default value
        self.assertEqual(self.instance.icon, "Font Awesome Icon")

    def test_str_method(self):
        '''Test the string method'''
        self.assertEqual(str(self.instance), "Test Name")
