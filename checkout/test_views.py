from django.test import TestCase
from django.urls import reverse
from django.conf import settings
# Use patch to mock an object (here the PaymentIntent)
from unittest.mock import patch
from django.contrib.messages import get_messages
from rooms.models import Room
from .models import Order


class TestCacheCheckoutDataView(TestCase):
    '''A class to test the cache checkout data view'''
    # Patch stops it making a real call to stripe
    @patch('stripe.PaymentIntent.modify')
    def test_cache_checkout_data_success(self, mock_modify):
        # Set up test POST data
        data = {
            'client_secret': 'test_secret_123',
            'room_id': '1',
            'check_in_date': '2024-11-05',
            'check_out_date': '2024-11-10',
            'adults': '2',
            'children': '1',
            'infants': '0',
            'save_info': 'true',
        }

        response = self.client.post(reverse('cache_checkout_data'), data)
        # Assert the modify method was called
        mock_modify.assert_called_once()
        # Assert response status code
        self.assertEqual(response.status_code, 200)

    @patch('stripe.PaymentIntent.modify', side_effect=Exception('Test Error'))
    def test_cache_checkout_data_error(self, mock_modify):
        '''Tests the error messages'''
        response = self.client.post(reverse('cache_checkout_data'), {})

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            str(messages[0]),
            'Sorry, your payment cannot be processed right now. '
            'Please try again later.'
        )


class TestCheckoutView(TestCase):
    '''Tests for the checkout view'''
    def test_checkout_renders_checkout_form(self):
        '''Test that the checkout view renders the checkout form'''
        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')
        self.assertIn('checkout_form', response.context)

    @patch('stripe.PaymentIntent.create')
    def test_payment_intent_creation(self, mock_intent_create):
        '''Tests the creation of a payment intent'''
        # Create room instance and test data
        room = Room.objects.create(id=1, price=100, image='test.jpg')
        data = {
            'direct_to_checkout': 'true',
            'room_id': room.id,
            'total_days': '3',
            'check_in_date': '2024-11-05',
            'check_out_date': '2024-11-08',
            'adults': '2',
            'children': '1',
            'infants': '0',
        }

        # Create a client_secret value
        mock_intent_create.return_value = {'client_secret': 'test_secret'}
        # Simulate a post request
        response = self.client.post(reverse('checkout'), data)

        # Check that the intent is created
        mock_intent_create.assert_called_once_with(
            amount=30000,
            currency=settings.STRIPE_CURRENCY
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')
        self.assertIn('client_secret', response.context)

    def test_checkout_payment_form_order_creation(self):
        data = {
            'payment_form': 'true',
            'full_name': 'Test User',
            'email': 'test@example.com',
            'phone_number': '123456789',
            'country': 'US',
            'postcode': '12345',
            'town_or_city': 'Test City',
            'street_address1': '123 Main St',
            'street_address2': '',
            'county': 'Test County',
            'total_cost': '300.00',
            'client_secret': 'test_secret',
        }

        response = self.client.post(reverse('checkout'), data)

        # Check an order was created
        order = Order.objects.get(email='test@example.com')
        self.assertEqual(order.full_name, 'Test User')
        self.assertEqual(order.order_total, 300.00)

        # Confirm success page is rendered
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/success.html')
        self.assertIn('order_number', response.context)
