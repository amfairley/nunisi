from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile, Trip
from django.apps import apps
from django.db.models.signals import post_save
from user_profile.signals import create_or_update_user_profile
from django.db.models import (
    CharField,
    BooleanField,
    ForeignKey,
    DateField,
    IntegerField,
    DecimalField,
)


class UserProfileModelTest(TestCase):
    '''Test the UserProfile model'''
    def setUp(self):
        '''Create a user so that the UserProfile can be created'''
        # Disable signal to prevent duplicate instances
        post_save.disconnect(
            receiver=create_or_update_user_profile,
            sender=User
        )
        # Create a User
        self.user = User.objects.create_user(
            username='testuser',
            password='password123'
        )
        # Trigger the signal to create a UserProfile
        create_or_update_user_profile(
            sender=User,
            instance=self.user,
            created=True
        )

    def test_userprofile_model_exists(self):
        '''Check that the app is installed and model defined'''
        self.assertTrue(apps.is_installed('user_profile'))
        self.assertIn(
            'UserProfile', [model.__name__ for model in apps.get_models()]
        )

    def test_user_profile_creation(self):
        '''Test the user profile is created with the user'''
        profile = UserProfile.objects.get(user=self.user)
        self.assertEqual(profile.user, self.user)

    def test_full_name_field(self):
        '''Test the full_name field'''
        # Get the 'full_name' field from the model
        field = UserProfile._meta.get_field('full_name')
        # Check that the field is a CharField
        self.assertIsInstance(field, CharField)
        self.assertEqual(field.get_internal_type(), 'CharField')
        # Check the max length of the CharField
        self.assertEqual(field.max_length, 150)
        # Check null status
        self.assertTrue(field.null)
        # Check blank status
        self.assertTrue(field.blank)

    def test_phone_number_field(self):
        '''Test the phone_number field'''
        # Get the 'phone_number' field from the model
        field = UserProfile._meta.get_field('phone_number')
        # Check that the field is a CharField
        self.assertIsInstance(field, CharField)
        self.assertEqual(field.get_internal_type(), 'CharField')
        # Check the max length of the CharField
        self.assertEqual(field.max_length, 20)
        # Check null status
        self.assertTrue(field.null)
        # Check blank status
        self.assertTrue(field.blank)

    def test_country_field(self):
        '''Test the country field'''
        # Get the 'country' field from the model
        field = UserProfile._meta.get_field('country')
        # Check that the field is a CharField
        self.assertIsInstance(field, CharField)
        self.assertEqual(field.get_internal_type(), 'CharField')
        # Check the max length of the CharField
        self.assertEqual(field.max_length, 2)
        # Check null status
        self.assertTrue(field.null)
        # Check blank status
        self.assertTrue(field.blank)

    def test_postcode_field(self):
        '''Test the postcode field'''
        # Get the 'postcode' field from the model
        field = UserProfile._meta.get_field('postcode')
        # Check that the field is a CharField
        self.assertIsInstance(field, CharField)
        self.assertEqual(field.get_internal_type(), 'CharField')
        # Check the max length of the CharField
        self.assertEqual(field.max_length, 20)
        # Check null status
        self.assertTrue(field.null)
        # Check blank status
        self.assertTrue(field.blank)

    def test_town_or_city_field(self):
        '''Test the town_or_city field'''
        # Get the 'town_or_city' field from the model
        field = UserProfile._meta.get_field('town_or_city')
        # Check that the field is a CharField
        self.assertIsInstance(field, CharField)
        self.assertEqual(field.get_internal_type(), 'CharField')
        # Check the max length of the CharField
        self.assertEqual(field.max_length, 40)
        # Check null status
        self.assertTrue(field.null)
        # Check blank status
        self.assertTrue(field.blank)

    def test_street_address1_field(self):
        '''Test the street_address1 field'''
        # Get the 'street_address1' field from the model
        field = UserProfile._meta.get_field('street_address1')
        # Check that the field is a CharField
        self.assertIsInstance(field, CharField)
        self.assertEqual(field.get_internal_type(), 'CharField')
        # Check the max length of the CharField
        self.assertEqual(field.max_length, 80)
        # Check null status
        self.assertTrue(field.null)
        # Check blank status
        self.assertTrue(field.blank)

    def test_street_address2_field(self):
        '''Test the street_address2 field'''
        # Get the 'street_address2' field from the model
        field = UserProfile._meta.get_field('street_address2')
        # Check that the field is a CharField
        self.assertIsInstance(field, CharField)
        self.assertEqual(field.get_internal_type(), 'CharField')
        # Check the max length of the CharField
        self.assertEqual(field.max_length, 80)
        # Check null status
        self.assertTrue(field.null)
        # Check blank status
        self.assertTrue(field.blank)

    def test_county_field(self):
        '''Test the county field'''
        # Get the 'county' field from the model
        field = UserProfile._meta.get_field('county')
        # Check that the field is a CharField
        self.assertIsInstance(field, CharField)
        self.assertEqual(field.get_internal_type(), 'CharField')
        # Check the max length of the CharField
        self.assertEqual(field.max_length, 80)
        # Check null status
        self.assertTrue(field.null)
        # Check blank status
        self.assertTrue(field.blank)

    def test_newsletter_field(self):
        '''Test the newsletter field'''
        # Get the 'newsletter' field from the model
        field = UserProfile._meta.get_field('newsletter')
        # Check that the field is a BooleanField
        self.assertIsInstance(field, BooleanField)
        self.assertEqual(field.get_internal_type(), 'BooleanField')

    def test_str_method(self):
        '''Test the __str__ method'''
        profile = UserProfile.objects.get(user=self.user)
        self.assertEqual(str(profile), self.user.username)

    def tearDown(self):
        '''Set up the signal again after the test'''
        post_save.connect(receiver=create_or_update_user_profile, sender=User)


class TripModelTest(TestCase):
    '''Test the Trip model'''
    def test_trip_model_exists(self):
        '''Check that the app is installed and model defined'''
        self.assertTrue(apps.is_installed('user_profile'))
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
