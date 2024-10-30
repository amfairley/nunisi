from django.test import TestCase
from django.urls import reverse
from .models import Room, Amenities


class AvailableRoomsViewTest(TestCase):
    '''Test the rooms view for available_rooms'''

    # Set up some room instances for testing
    @classmethod
    def setUpTestData(cls):
        # Create amenities instances
        cls.bed = Amenities.objects.create(name='Bed')
        cls.double_bed = Amenities.objects.create(name='Double Bed')
        # Create room instances
        cls.room1 = Room.objects.create(
            name="Room 1",
            sanitised_name="Room One",
            price=100,
            amenities=[cls.bed.pk],
            unavailability=[],
        )
        cls.room2 = Room.objects.create(
            name="Room 2",
            sanitised_name="Room Two",
            price=150,
            amenities=[cls.double_bed.pk],
            unavailability=[('2024, 11, 1')],
        )

    def test_view_renders(self):
        '''Test that the view renders correctly'''
        response = self.client.get(reverse('available_rooms'), {
            'check_in_date': '2024-10-15',
            'check_out_date': '2024-10-20',
            'adults': 1,
            'children': 1,
            'infants': 0,
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'rooms/available_rooms.html')
        self.assertIn('valid_rooms', response.context)

    def test_room_unavailability(self):
        """Test that room 2 is not shown due to unavailability"""
        response = self.client.get(reverse('available_rooms'), {
            'check_in_date': '2024-10-31',
            'check_out_date': '2024-11-02',
            'adults': 2,
            'children': 0,
            'infants': 1,
        })
        valid_rooms = response.context['valid_rooms']
        self.assertEqual(len(valid_rooms), 1)

    def test_total_cost_calculation(self):
        """Test the total cost calculation"""
        response = self.client.get(reverse('available_rooms'), {
            'check_in_date': '2024-10-15',
            'check_out_date': '2024-10-18',
            'adults': 1,
            'children': 0,
            'infants': 0,
        })
        # Get valid_rooms from the context
        valid_rooms = response.context['valid_rooms']
        for room in valid_rooms:
            total_cost = room['room'].price * response.context['total_days']
            self.assertEqual(room['total_cost'], total_cost)
