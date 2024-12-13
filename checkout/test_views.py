from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
# Use patch to mock an object (here the PaymentIntent)
from unittest.mock import patch
from django.contrib.messages import get_messages
from rooms.models import Room
from checkout.models import Order
from user_profile.models import UserProfile
import json


class TestCacheCheckoutDataView(TestCase):
    '''A class to test the cache checkout data view'''
    def setUp(self):
        """Set up test data and a logged-in user."""
        # Create a user and log in
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='password'
        )
        self.client.login(
            username='testuser',
            password='password'
        )
        # Create a test room
        self.room = Room.objects.create(name='Test Room', price=100)
        self.url = reverse('cache_checkout_data')
        # Create some test data
        self.valid_data = {
            'client_secret': 'test',
            'room_id': str(self.room.id),
            'check_in_date': '2024-12-30',
            'check_out_date': '2024-12-31',
            'adults': '2',
            'children': '1',
            'infants': '0',
            'save_info': 'true',
            'total_cost': '200.00',
        }

    # Patch stops it making a real call to stripe
    @patch('stripe.PaymentIntent.modify')
    def test_cache_checkout_data_success(self, mock_modify):
        """Test successful Stripe API call."""
        mock_modify.return_value = True
        response = self.client.post(self.url, self.valid_data)
        # Assert the modify method was called with the correct arguments
        mock_modify.assert_called_once_with(
            'test',
            metadata={
                'trip_data': json.dumps({
                    'room': str(self.room.id),
                    'start_date': '2024-12-30',
                    'end_date': '2024-12-31',
                    'adults': '2',
                    'children': '1',
                    'infants': '0',
                    'cost': '200.00',
                }),
                'save_info': 'true',
                'user_email': 'testuser@example.com',
            }
        )
        # Assert response status code
        self.assertEqual(response.status_code, 200)

    @patch('stripe.PaymentIntent.modify', side_effect=Exception('Test Error'))
    def test_cache_checkout_data_error(self, mock_modify):
        """Test Stripe API call failure."""
        response = self.client.post(self.url, self.valid_data)

        # Assert the error message is added to messages
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]),
            'Sorry, your payment cannot be processed right now. '
            'Please try again later.'
        )

        # Assert response status code
        self.assertEqual(response.status_code, 400)

    def test_cache_checkout_data_missing_client_secret(self):
        """Test missing client_secret in POST data."""
        invalid_data = self.valid_data.copy()
        invalid_data.pop('client_secret')

        response = self.client.post(self.url, invalid_data)

        # Assert response status code
        self.assertEqual(response.status_code, 400)

        # Assert error message
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn(
            'Sorry, your payment cannot be processed right now.',
            str(messages[0])
        )


class TestCheckoutView(TestCase):
    '''Tests for the checkout view'''
    def setUp(self):
        self.client = Client()
        self.checkout_url = reverse('checkout')
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='password'
        )
        self.room = Room.objects.create(
            name='testroom',
            sanitised_name='Test Room',
            amenities=[1],
            description='Test description',
            image='test_image.png',
            price=100.00,
        )
        self.user_profile = UserProfile.objects.get(user=self.user)

    def test_checkout_renders_checkout_form(self):
        '''Test that the checkout view renders the checkout form'''
        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')
        self.assertIn('checkout_form', response.context)

    @patch('stripe.PaymentIntent.create')
    def test_checkout_context(self, mock_stripe):
        '''Test if the context passed is correct'''
        mock_stripe.return_value = {'client_secret': 'test'}
        post_data = {
            'direct_to_checkout': 'true',
            'room_id': self.room.id,
            'total_days': '2',
            'check_in_date': '2024-12-20',
            'check_out_date': '2024-12-22',
            'adults': '2',
            'children': '1',
            'infants': '',
        }
        self.client.login(username='testuser', password='password')
        response = self.client.post(self.checkout_url, post_data)
        # Check the passed context
        context = response.context
        self.assertEqual(int(context['room_id']), self.room.id)
        self.assertEqual(context['room'], self.room)
        self.assertEqual(context['total_days'], '2')
        self.assertEqual(context['check_in_date'], '2024-12-20')
        self.assertEqual(context['sanitised_check_in_date'], '20-Dec-2024')
        self.assertEqual(context['check_out_date'], '2024-12-22')
        self.assertEqual(context['sanitised_check_out_date'], '22-Dec-2024')
        self.assertEqual(context['total_guests'], 3)
        self.assertEqual(int(context['adults']), 2)
        self.assertEqual(int(context['children']), 1)
        self.assertEqual(int(context['infants']), 0)
        self.assertEqual(float(context['total_cost']), 200.00)
        self.assertEqual(context['client_secret'], 'test')

    @patch('stripe.PaymentIntent.create')
    def test_checkout_payment_form(self, mock_stripe):
        '''Test payment processing'''
        mock_stripe.return_value = {'client_secret': 'test'}
        # Change some data and tick save info
        post_data = {
            'payment_form': '1',
            'save_info': True,
            'full_name': 'Updated User',
            'email': 'test_user@example.com',
            'phone_number': '0987654321',
            'country': 'US',
            'postcode': '54321',
            'town_or_city': 'Updated City',
            'street_address1': '456 Updated Street',
            'street_address2': '',
            'total_cost': '200.00',
            'client_secret': 'test',
        }

        self.client.login(username='testuser', password='password')
        response = self.client.post(self.checkout_url, post_data)

        self.assertEqual(response.status_code, 200)
        # Check it redirects to success page
        self.assertTemplateUsed(response, 'checkout/success.html')
        # Test the updates user profile keys
        self.user_profile.refresh_from_db()
        self.assertEqual(self.user_profile.full_name, 'Updated User')
        self.assertEqual(self.user_profile.phone_number, '0987654321')
        self.assertEqual(self.user_profile.country, 'US')
        self.assertEqual(self.user_profile.town_or_city, 'Updated City')
        self.assertEqual(
            self.user_profile.street_address1,
            '456 Updated Street'
        )

        # Verify Order creation
        order = Order.objects.first()
        self.assertIsNotNone(order)
        self.assertEqual(order.full_name, 'Updated User')
        self.assertEqual(order.email, 'test_user@example.com')
        self.assertEqual(order.phone_number, '0987654321')
        self.assertEqual(order.country, 'US')
        self.assertEqual(order.town_or_city, 'Updated City')
        self.assertEqual(order.street_address1, '456 Updated Street')
        self.assertEqual(order.stripe_pid, 'test')
        self.assertEqual(order.order_total, 200.00)
