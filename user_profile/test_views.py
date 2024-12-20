from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import UserProfile
from allauth.account.models import EmailAddress


class UserProfileTests(TestCase):
    def setUp(self):
        # Create a user and a profile
        self.user = User.objects.create_user(
            username='testuser',
            password='password'
        )
        self.user_profile = UserProfile.objects.get(user=self.user)
        EmailAddress.objects.create(
            user=self.user,
            email='testuser@example.com',
            verified=True,
            primary=True
        )
        self.client.login(username='testuser', password='password')

    def test_user_profile_view(self):
        """Test the user_profile view uses the correct template and context"""
        response = self.client.get(reverse('user_profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_profile/user_profile.html')
        self.assertIn('user_profile', response.context)
        self.assertIn('email_addresses', response.context)

    def test_edit_profile_view_get(self):
        """Test the edit_profile view"""
        response = self.client.get(reverse('edit_profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_profile/edit_profile.html')
        self.assertIn('form', response.context)
        self.assertIn('user_profile', response.context)

    def test_edit_profile_updated(self):
        """Test the edit_profile updating with new data"""
        response = self.client.post(reverse('edit_profile'), {
            'full_name': 'testname',
            'phone_number': '123',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_profile/user_profile.html')
        self.assertContains(response, "Account updated.")

    def test_delete_user_view(self):
        """Test the delete_user view"""
        response = self.client.get(reverse('delete_user', args=[self.user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_profile/delete_user.html')

    def test_delete_user_view_delete(self):
        """Test the delete_user functionality"""
        response = self.client.post(
            reverse('delete_user', args=[self.user.id])
        )
        self.assertRedirects(response, reverse('delete_successful'))
        # Check the user has been deleted
        self.assertFalse(User.objects.filter(id=self.user.id).exists())

    def test_delete_successful_view(self):
        """Test the delete_successful view."""
        response = self.client.get(reverse('delete_successful'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            'user_profile/delete_successful.html'
        )
