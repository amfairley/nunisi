from django.test import TestCase, Client
from .models import UserProfile
from .forms import EditProfileForm
from django.contrib.auth.models import User


class EditProfileFormTest(TestCase):
    '''Test the edit user profile form'''
    def setUp(self):
        '''Create a user profile to edit'''
        # Create a user and log them in
        self.user = User.objects.create_user(
            username="testuser",
            password="password123"
        )
        self.client = Client()
        self.client.login(username="testuser", password="password123")
        self.user_profile = UserProfile.objects.get(user=self.user)

    def test_form_valid_data(self):
        """Test form with valid data"""
        form_data = {
            'full_name': 'testname',
            'phone_number': '123',
            'street_address1': 'testaddress1',
            'street_address2': 'testaddress2',
            'town_or_city': 'testtown',
            'county': 'testcounty',
            'country': 'GB',
            'postcode': 'test',
            'newsletter': True,
        }
        form = EditProfileForm(data=form_data, instance=self.user_profile)
        self.assertTrue(form.is_valid())

        # Save the form and check that it has been updated correctly
        profile = form.save()
        self.assertEqual(profile.full_name, "testname")
        self.assertEqual(profile.phone_number, "123")
        self.assertEqual(profile.street_address1, "testaddress1")
        self.assertEqual(profile.street_address2, "testaddress2")
        self.assertEqual(profile.town_or_city, "testtown")
        self.assertEqual(profile.county, "testcounty")
        self.assertEqual(profile.country, "GB")
        self.assertEqual(profile.postcode, "test")
        self.assertEqual(profile.newsletter, True)
