from django.test import TestCase
from django.urls import reverse


class TestCheckoutView(TestCase):
    '''A class to test the checkout views'''
    def test_checkout_view_works(self):
        '''A test to check that the correct template is used and page loads'''
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')

    def test_post_data_collection(self):
        '''Check that the posted data is being accessed correctly'''
        # Define a URL
        url = reverse('checkout')

        # Create sample data
        sample_data = {
            'room_id': 1,
            'total_days': 3,
            'check_in_date': '2024-11-01',
            'check_out_date': '2024-11-04',
            'adults': 2,
            'children': 1,
            'infants': 0,
        }

        # Send a POST request
        response = self.client.post(url, data=sample_data)

        # Check that the values match
        self.assertEqual(
            int(response.context['room_id']), sample_data['room_id']
        )
        self.assertEqual(
            int(response.context['total_days']), sample_data['total_days']
        )
        self.assertEqual(
            response.context['check_in_date'], sample_data['check_in_date']
        )
        self.assertEqual(
            response.context['check_out_date'], sample_data['check_out_date']
        )
        self.assertEqual(
            int(response.context['adults']), sample_data['adults']
        )
        self.assertEqual(
            int(response.context['children']), sample_data['children']
        )
        self.assertEqual(
            int(response.context['infants']), sample_data['infants']
        )
