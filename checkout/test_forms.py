from django.test import TestCase
from .forms import CheckoutForm


class CheckoutFormTest(TestCase):
    '''Tests for the checkout form'''
    # Create a form with all required fields

    @classmethod
    def setUpTestData(cls):
        '''Create a form of required fields to test unrequired fields'''
        cls.required_form_data = {
            'full_name': 'Test User',
            'email': 'test@gmail.com',
            'phone_number': '1234567890',
            'country': 'GB',
            'town_or_city': 'London',
            'street_address1': '123 Test Street',
        }

    def test_checkout_form_exists(self):
        '''Tests that the checkout form exists and is defined'''
        form = CheckoutForm()
        self.assertIsInstance(form, CheckoutForm)

    def test_unrequired_fields(self):
        form = CheckoutForm(data=self.required_form_data)
        self.assertTrue(form.is_valid())
        self.assertNotIn('postcode', form.errors)
        self.assertNotIn('street_address2', form.errors)
        self.assertNotIn('county', form.errors)

    def test_full_name_field(self):
        '''Test the full name field'''
        # Test it is required
        form = CheckoutForm({'full_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors)
        # Test max length
        max_length = form.fields['full_name'].max_length
        self.assertEqual(max_length, 150)
        # Test label name
        form_label = form['full_name'].label_tag()
        self.assertEqual(
            form_label,
            '<label for="id_full_name">Full Name:</label>'
        )

    def test_email_field(self):
        '''Test the email field'''
        # Test if it is required
        form = CheckoutForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)
        # Test max length
        max_length = form.fields['email'].max_length
        self.assertEqual(max_length, 254)
        # Test label name
        form_label = form['email'].label_tag()
        self.assertEqual(
            form_label,
            '<label for="id_email">Email Address:</label>'
        )

    def test_phone_number_field(self):
        '''Test the phone_number field'''
        # Test if it is required
        form = CheckoutForm({'phone_number': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('phone_number', form.errors)
        # Test max length
        max_length = form.fields['phone_number'].max_length
        self.assertEqual(max_length, 20)
        # Test label name
        form_label = form['phone_number'].label_tag()
        self.assertEqual(
            form_label,
            '<label for="id_phone_number">Phone Number:</label>'
        )

    def test_country_field(self):
        '''Test the country field'''
        # Test if the field is required
        form = CheckoutForm({'country': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('country', form.errors)

        # Test that the field has the correct label
        form_label = form.fields['country'].label
        self.assertEqual(form_label, "Country")

    def test_postcode_field(self):
        '''Test the postcode field'''
        form = CheckoutForm({'postcode': ''})
        # Test max length
        max_length = form.fields['postcode'].max_length
        self.assertEqual(max_length, 20)
        # Test label name
        form_label = form['postcode'].label_tag()
        self.assertEqual(
            form_label,
            '<label for="id_postcode">Postcode:</label>'
        )

    def test_town_or_city_field(self):
        '''Test the town_or_city field'''
        # Test if it is required
        form = CheckoutForm({'town_or_city': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('town_or_city', form.errors)
        # Test max length
        max_length = form.fields['town_or_city'].max_length
        self.assertEqual(max_length, 40)
        # Test label name
        form_label = form['town_or_city'].label_tag()
        self.assertEqual(
            form_label,
            '<label for="id_town_or_city">Town or City:</label>'
        )

    def test_street_address1_field(self):
        '''Test the street_address1 field'''
        # Test if it is required
        form = CheckoutForm({'street_address1': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('street_address1', form.errors)
        # Test max length
        max_length = form.fields['street_address1'].max_length
        self.assertEqual(max_length, 80)
        # Test label name
        form_label = form['street_address1'].label_tag()
        self.assertEqual(
            form_label,
            '<label for="id_street_address1">Street Address Line 1:</label>'
        )

    def test_street_address2_field(self):
        '''Test the street_address2 field'''
        form = CheckoutForm({'street_address2': ''})
        # Test max length
        max_length = form.fields['street_address2'].max_length
        self.assertEqual(max_length, 80)
        # Test label name
        form_label = form['street_address2'].label_tag()
        self.assertEqual(
            form_label,
            '<label for="id_street_address2">Street Address Line 2:</label>'
        )

    def test_county_field(self):
        '''Test the county field'''
        form = CheckoutForm({'county': ''})
        # Test max length
        max_length = form.fields['county'].max_length
        self.assertEqual(max_length, 80)
        # Test label name
        form_label = form['county'].label_tag()
        self.assertEqual(
            form_label,
            '<label for="id_county">County:</label>'
        )
