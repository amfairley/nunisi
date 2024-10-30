from django.test import TestCase


class TestCheckoutView(TestCase):
    '''A class to test the checkout views'''
    def test_checkout_view_works(self):
        '''A test to check that the correct template is used and page loads'''
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')
