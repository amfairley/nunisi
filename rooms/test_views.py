from django.test import TestCase, Client
from django.urls import reverse
from datetime import date, timedelta


class AvailableRoomsViewTests(TestCase):
    '''Test the rooms view for available_rooms'''
    def setUp(self):
        self.client = Client()
        self.url = reverse('available_rooms')

    def test_available_rooms_renders_correctly(self):
        '''Test the correct template is used and works'''
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'rooms/available_rooms.html')

    def test_available_rooms_context(self):
        '''Test that the correct data is in the context'''
        response = self.client.get(self.url)
        self.assertIn('rooms', response.context)
        self.assertIn('amenities', response.context)
        self.assertIn('booking_form', response.context)
        self.assertIn('booking_form_desktop', response.context)

    def test_available_rooms_valid_data(self):
        '''Test valid data'''
        # Set up data
        valid_data = {
            'mobile-check_in_date': date.today(),
            'mobile-check_out_date': date.today() + timedelta(days=2),
            'mobile-adults': 2,
        }
        response = self.client.post(self.url, valid_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('valid_rooms', response.context)

    def test_available_room_invalid_data(self):
        '''Test invalid data'''
        invalid_data = {'mobile-check_in_date': 'invalid-date'}
        response = self.client.post(self.url, invalid_data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['booking_form'].is_valid())
