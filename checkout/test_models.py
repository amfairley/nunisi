from django.test import TestCase
from django.apps import apps
from .models import Order
from django.db.models import (
    CharField,
    EmailField,
    DateTimeField,
    DecimalField
)
from django_countries.fields import CountryField


class RoomModelTest(TestCase):
    '''Tests for the Room model'''
    def test_model_exists(self):
        '''Check that the app is installed and model defined'''
        self.assertTrue(apps.is_installed('checkout'))
        self.assertIn(
            'Order', [model.__name__ for model in apps.get_models()]
        )

    def test_order_number_field(self):
        '''Test the order number field'''
        # Get the 'order_number' field from the model
        field = Order._meta.get_field('order_number')
        # Check that the field is a CharField
        self.assertIsInstance(field, CharField)
        self.assertEqual(field.get_internal_type(), 'CharField')
        # Check the max length of the CharField
        self.assertEqual(field.max_length, 32)
        # Check null status
        self.assertFalse(field.null)
        # Check editable status
        self.assertFalse(field.editable)

    def test_full_name_field(self):
        '''Test the full name field'''
        # Get the 'full_name' field from the model
        field = Order._meta.get_field('full_name')
        # Check that the field is a CharField
        self.assertIsInstance(field, CharField)
        self.assertEqual(field.get_internal_type(), 'CharField')
        # Check the max length of the CharField
        self.assertEqual(field.max_length, 150)
        # Check null status
        self.assertFalse(field.null)
        # Check blank status
        self.assertFalse(field.blank)

    def test_email_field(self):
        '''Test the email field'''
        # Get the 'email' field from the model
        field = Order._meta.get_field('email')
        # Check that the field is a EmailField
        self.assertIsInstance(field, EmailField)
        self.assertEqual(field.get_internal_type(), 'CharField')
        # Check the max length of the EmailField
        self.assertEqual(field.max_length, 254)
        # Check null status
        self.assertFalse(field.null)
        # Check blank status
        self.assertFalse(field.blank)

    def test_phone_number_field(self):
        '''Test the phone_number field'''
        # Get the 'phone_number' field from the model
        field = Order._meta.get_field('phone_number')
        # Check that the field is a CharField
        self.assertIsInstance(field, CharField)
        self.assertEqual(field.get_internal_type(), 'CharField')
        # Check the max length of the CharField
        self.assertEqual(field.max_length, 20)
        # Check null status
        self.assertFalse(field.null)
        # Check blank status
        self.assertFalse(field.blank)

    def test_country_field(self):
        '''Test the country field'''
        # Get the 'country' field from the model
        field = Order._meta.get_field('country')
        # Check that the field is a CountryField
        self.assertIsInstance(field, CountryField)
        self.assertEqual(field.get_internal_type(), 'CharField')
        # Check the blank label
        self.assertEqual(field.blank_label, 'Country *')
        # Check null status
        self.assertFalse(field.null)
        # Check blank status
        self.assertFalse(field.blank)

    def test_postcode_field(self):
        '''Test the postcode field'''
        # Get the 'postcode' field from the model
        field = Order._meta.get_field('postcode')
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
        '''Test the town or city field'''
        # Get the 'town_or_city' field from the model
        field = Order._meta.get_field('town_or_city')
        # Check that the field is a CharField
        self.assertIsInstance(field, CharField)
        self.assertEqual(field.get_internal_type(), 'CharField')
        # Check the max length of the CharField
        self.assertEqual(field.max_length, 40)
        # Check null status
        self.assertFalse(field.null)
        # Check blank status
        self.assertFalse(field.blank)

    def test_street_address1_field(self):
        '''Test the street address 1 field'''
        # Get the 'street_address1' field from the model
        field = Order._meta.get_field('street_address1')
        # Check that the field is a CharField
        self.assertIsInstance(field, CharField)
        self.assertEqual(field.get_internal_type(), 'CharField')
        # Check the max length of the CharField
        self.assertEqual(field.max_length, 80)
        # Check null status
        self.assertFalse(field.null)
        # Check blank status
        self.assertFalse(field.blank)

    def test_street_address2_field(self):
        '''Test the street address 2 field'''
        # Get the 'street_address2' field from the model
        field = Order._meta.get_field('street_address2')
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
        field = Order._meta.get_field('county')
        # Check that the field is a CharField
        self.assertIsInstance(field, CharField)
        self.assertEqual(field.get_internal_type(), 'CharField')
        # Check the max length of the CharField
        self.assertEqual(field.max_length, 80)
        # Check null status
        self.assertTrue(field.null)
        # Check blank status
        self.assertTrue(field.blank)

    def test_date_field(self):
        '''Test the date field'''
        # Get the 'date' field from the model
        field = Order._meta.get_field('date')
        # Check that the field is a DateTimeField
        self.assertIsInstance(field, DateTimeField)
        self.assertEqual(field.get_internal_type(), 'DateTimeField')
        # Check the auto_now_add status
        self.assertTrue(field.auto_now_add)

    def test_order_total_field(self):
        '''Test the order_total field'''
        # Get the 'order_total' field from the model
        field = Order._meta.get_field('order_total')
        # Check that the field is a DecimalField
        self.assertIsInstance(field, DecimalField)
        self.assertEqual(field.get_internal_type(), 'DecimalField')
        # Check the max length of the DecimalField
        self.assertEqual(field.max_digits, 10)
        # Check the decimal places
        self.assertEqual(field.decimal_places, 2)
        # Check null status
        self.assertFalse(field.null)
        # Check default value
        self.assertEqual(field.default, 0)

    def test_generate_order_number(self):
        '''Test the generate order number method'''
        # Create an instance to check
        order = Order()
        # Create an order number using the method
        order_number = order._generate_order_number()
        # Check that the order number is a string
        self.assertIsInstance(order_number, str)
        # Check the length of the order number
        self.assertEqual(len(order_number), 32)
        # Check that the order number is uppercase
        self.assertTrue(order_number.isupper())

    def test_order_number_uniqueness(self):
        '''
        Check that the same order number is not created for 2 orders
        '''
        # Create 2 orders
        order1 = Order()
        order2 = Order()
        # Create 2 order_numbers
        order_number_1 = order1._generate_order_number()
        order_number_2 = order2._generate_order_number()
        # Check that they are not equal
        self.assertNotEqual(order_number_1, order_number_2)

    def test_add_order_number_on_save(self):
        '''Test that an order without an order number is assigned one'''
        # Create an instance without an order number
        order = Order()
        # Save the order
        order.save()
        # Check that it has an order number
        self.assertIsNotNone(order.order_number)

    def test_str_method(self):
        '''Test the Order string method'''
        # Create an instance and save it to add an order number
        order = Order()
        order.save()
        # Get the order number
        order_number = order.order_number
        # Check that the string method returns this order number
        self.assertEqual(order.__str__(), order_number)
