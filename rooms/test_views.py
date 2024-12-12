from django.test import TestCase, Client
from django.urls import reverse
from datetime import date, timedelta
from django.contrib.auth.models import User
from .models import Room, Amenities


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


class RoomsSuperuserViewTests(TestCase):
    '''Test the rooms superuser view'''
    def setUp(self):
        '''Create objects to test the Superuser rooms view'''
        # Staff
        self.staff_user = User.objects.create_user(
            username='admin', password='password123', is_staff=True
        )
        # Normal user
        self.non_staff_user = User.objects.create_user(
            username='user', password='password123', is_staff=False
        )
        self.client = Client()

    def test_access_by_staff_user(self):
        """Test that the view is accessible to staff users."""
        self.client.login(username='admin', password='password123')
        response = self.client.get(reverse('rooms_superuser'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'rooms/rooms_superuser.html')

    def test_access_by_normal_user(self):
        """Test that the view denies access to non-staff users."""
        self.client.login(username='user', password='password123')
        response = self.client.get(reverse('rooms_superuser'))
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('admin:login'), response.url)

    def test_access_without_login(self):
        """Test that the view denies access to unauthenticated users."""
        response = self.client.get(reverse('rooms_superuser'))
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('admin:login'), response.url)


class AddRoomViewTest(TestCase):
    '''Test the add room view'''
    def setUp(self):
        '''Create objects to test the add rooms view'''
        # Staff
        self.staff_user = User.objects.create_user(
            username='admin', password='password123', is_staff=True
        )
        # Normal user
        self.non_staff_user = User.objects.create_user(
            username='user', password='password123', is_staff=False
        )
        self.client = Client()

        # Create sample amenities
        self.amenity1 = Amenities.objects.create(
            name="bed",
            sanitised_name="Bed",
            icon="bed-icon"
        )

        self.amenity2 = Amenities.objects.create(
            name="wifi",
            sanitised_name="WiFi",
            icon="wifi-icon"
        )

        self.client = Client()

    def test_access_by_staff_user(self):
        """Test that the view is accessible to staff users."""
        self.client.login(username='admin', password='password123')
        response = self.client.get(reverse('add_room'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'rooms/add_room.html')

    def test_access_by_normal_user(self):
        """Test that the view denies access to non-staff users."""
        self.client.login(username='user', password='password123')
        response = self.client.get(reverse('add_room'))
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('admin:login'), response.url)

    def test_access_without_login(self):
        """Test that the view denies access to unauthenticated users."""
        response = self.client.get(reverse('add_room'))
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('admin:login'), response.url)

    def test_add_room_valid_data(self):
        """Test adding a room with valid data."""
        # Log in to access the view
        self.client.login(username='admin', password='password123')
        # Create valid data
        form_data = {
            'name': "new_room",
            'sanitised_name': "New Room",
            'amenities': [1, 2],
            'description': "A new room description",
            'price': 10.00,
        }
        response = self.client.post(reverse('add_room'), data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Room.objects.exists())

    def test_add_room_invalid_data(self):
        """Test adding a room with invalid data."""
        # Log in to access the view
        self.client.login(username='admin', password='password123')
        # Invalid data
        form_data = {
            'name': '',
            'description': '',
            'amenities': [],
            'price': -10.00,
        }
        response = self.client.post(reverse('add_room'), data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'rooms/add_room.html')
        self.assertIn('form', response.context)
        self.assertFalse(response.context['form'].is_valid())


class EditRoomViewTest(TestCase):
    '''Test the edit room view'''
    def setUp(self):
        '''Create objects to test the edit rooms view'''
        # Staff
        self.staff_user = User.objects.create_user(
            username='admin', password='password123', is_staff=True
        )
        # Normal user
        self.non_staff_user = User.objects.create_user(
            username='user', password='password123', is_staff=False
        )
        self.client = Client()

        # Create sample amenities
        self.amenity1 = Amenities.objects.create(
            name="bed",
            sanitised_name="Bed",
            icon="bed-icon"
        )

        self.amenity2 = Amenities.objects.create(
            name="wifi",
            sanitised_name="WiFi",
            icon="wifi-icon"
        )

        # Create sample room
        self.room = Room.objects.create(
            name="test_room",
            sanitised_name="Test Room",
            amenities=[1, 2],
            description="A room for testing",
            image_url=None,
            image=None,
            price=100.00,
            unavailability=["2024-12-20"]
        )

        self.url = reverse('edit_room', args=[self.room.id])

    def test_access_by_staff_user(self):
        """Test that the view is accessible to staff users."""
        self.client.login(username='admin', password='password123')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'rooms/edit_room.html')

    def test_access_by_normal_user(self):
        """Test that the view denies access to non-staff users."""
        self.client.login(username='user', password='password123')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('admin:login'), response.url)

    def test_access_without_login(self):
        """Test that the view denies access to unauthenticated users."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('admin:login'), response.url)


class DeleteRoomViewTest(TestCase):
    '''Test the delete room view'''
    def setUp(self):
        '''Create objects to test the delete rooms view'''
        # Staff
        self.staff_user = User.objects.create_user(
            username='admin', password='password123', is_staff=True
        )
        # Normal user
        self.non_staff_user = User.objects.create_user(
            username='user', password='password123', is_staff=False
        )

        self.client = Client()

        # Create sample amenities
        self.amenity1 = Amenities.objects.create(
            name="bed",
            sanitised_name="Bed",
            icon="bed-icon"
        )

        self.amenity2 = Amenities.objects.create(
            name="wifi",
            sanitised_name="WiFi",
            icon="wifi-icon"
        )

        # Create sample room
        self.room = Room.objects.create(
            name="test_room",
            sanitised_name="Test Room",
            amenities=[1, 2],
            description="A room for testing",
            image_url=None,
            image=None,
            price=100.00,
            unavailability=["2024-12-20"]
        )

        self.url = reverse('delete_room', args=[self.room.id])

    def test_access_by_staff_user(self):
        """Test that the view is accessible to staff users."""
        self.client.login(username='admin', password='password123')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'rooms/delete_room.html')

    def test_access_by_normal_user(self):
        """Test that the view denies access to non-staff users."""
        self.client.login(username='user', password='password123')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('admin:login'), response.url)

    def test_access_without_login(self):
        """Test that the view denies access to unauthenticated users."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('admin:login'), response.url)

    def test_room_deletion(self):
        """Test that the room is deleted"""
        # Log in to access the view
        self.client.login(username='admin', password='password123')

        # Ensure the room exists before the request
        self.assertTrue(Room.objects.filter(id=self.room.id).exists())

        # POST request to delete the room
        response = self.client.post(self.url)

        # Assert the room is deleted
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('rooms_superuser'))
        self.assertFalse(Room.objects.filter(id=self.room.id).exists())
