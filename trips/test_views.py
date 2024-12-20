from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from reviews.models import Review
from trips.models import Trip
from user_profile.models import UserProfile
from rooms.models import Room
from datetime import timedelta
from django.utils.timezone import now


class TripsUserViewTests(TestCase):
    """Tests for the user trips view."""

    def setUp(self):
        '''Set up for user trips tests'''
        # Create a user and log them in
        self.user = User.objects.create_user(
            username="testuser",
            password="password123"
        )
        self.client = Client()
        self.client.login(username="testuser", password="password123")
        self.user_profile = UserProfile.objects.get(user=self.user)
        # Create a second user to check thier trips do not get called
        self.other_user = User.objects.create_user(
            username="otheruser",
            password="password123"
        )
        self.other_profile = UserProfile.objects.get(user=self.other_user)
        # Create instances for testing: Room
        self.room = Room.objects.create(
            name="new_room",
            sanitised_name="New Room",
            amenities=[1, 2],
            description="A new room description",
            price=10.00,
        )
        # Create instances for testing:
        # Future trip
        # Past trip with review
        # Other profile trip
        today = now().date()
        self.upcoming_trip = Trip.objects.create(
            profile=self.user_profile,
            room=self.room,
            start_date=today + timedelta(days=1),
            end_date=today + timedelta(days=2),
            adults=2,
            cost=10.00,
        )
        self.past_trip = Trip.objects.create(
            profile=self.user_profile,
            room=self.room,
            start_date=today - timedelta(days=2),
            end_date=today - timedelta(days=1),
            adults=2,
            cost=10.00,
        )
        self.review = Review.objects.create(
            trip=self.past_trip,
            content="Great stay!",
            rating=5
        )
        self.other_trip = Trip.objects.create(
            profile=self.other_profile,
            room=self.room,
            start_date=today + timedelta(days=3),
            end_date=today + timedelta(days=4),
            adults=2,
            cost=30.00,
        )
        # URL for the add_review view
        self.url = reverse('trips_user')

    def test_trips_renders_correctly(self):
        """Test that the trips view renders correctly."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'trips/trips.html')

    def test_only_user_trips_loaded(self):
        """Test that the view returns trips only for the logged-in user."""
        response = self.client.get(self.url)
        trips = response.context['trips']
        self.assertIn(self.upcoming_trip, trips)
        self.assertIn(self.past_trip, trips)
        self.assertNotIn(self.other_trip, trips)

    def test_upcoming_and_past_trips(self):
        """Test the separation of upcoming and past trips."""
        response = self.client.get(self.url)
        upcoming_trips = response.context['upcoming_trips']
        past_trips = response.context['past_trips']
        self.assertIn(self.upcoming_trip, upcoming_trips)
        self.assertEqual(len(upcoming_trips), 1)
        self.assertEqual(len(past_trips), 1)
        self.assertEqual(past_trips[0]['trip'], self.past_trip)
        self.assertEqual(past_trips[0]['review'], self.review)

    def test_sorting_of_past_trips(self):
        """Test sorting functionality for past trips."""
        today = now().date()
        older_trip = Trip.objects.create(
            profile=self.user_profile,
            room=self.room,
            start_date=today - timedelta(days=5),
            end_date=today - timedelta(days=4),
            adults=2,
            cost=15.00,
        )
        response = self.client.get(self.url + '?sort=oldest_first')
        past_trips = response.context['past_trips']
        # Check the first one is the oldest trip
        self.assertEqual(past_trips[0]['trip'], older_trip)

        response = self.client.get(self.url + '?sort=newest_first')
        past_trips = response.context['past_trips']
        # Check the first one is the newset trip
        self.assertEqual(past_trips[0]['trip'], self.past_trip)

    def test_pagination_of_past_trips(self):
        """Test pagination functionality for past trips."""
        # Make 5 trips to paginate
        for i in range(5):
            Trip.objects.create(
                profile=self.user_profile,
                room=self.room,
                start_date=now().date() - timedelta(days=i + 3),
                end_date=now().date() - timedelta(days=i + 2),
                adults=2,
                cost=20.00,
            )
        response = self.client.get(self.url + '?page=1')
        # Test number of trips per page
        self.assertEqual(len(response.context['page_obj']), 1)

    def test_redirects_for_unauthenticated_user(self):
        """Test that an unauthenticated user cannot access the trips page"""
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)


class CancelTripViewTests(TestCase):
    """Tests for the cancel_trip view."""
    def setUp(self):
        '''Set up for the cancel trip view tests'''
        # Create a user and log them in
        self.user = User.objects.create_user(
            username="testuser",
            password="password123"
        )
        self.client = Client()
        self.client.login(username="testuser", password="password123")
        self.user_profile = UserProfile.objects.get(user=self.user)

        # Create a room
        self.room = Room.objects.create(
            name="Test Room",
            sanitised_name="test-room",
            amenities=[],
            description="A test room",
            price=50.00,
        )

        # Create upcoming and past trips
        self.upcoming_trip = Trip.objects.create(
            profile=self.user_profile,
            room=self.room,
            start_date=now().date() + timedelta(days=5),
            end_date=now().date() + timedelta(days=10),
            adults=2,
            cost=500.00,
        )
        self.past_trip = Trip.objects.create(
            profile=self.user_profile,
            room=self.room,
            start_date=now().date() - timedelta(days=10),
            end_date=now().date() - timedelta(days=5),
            adults=2,
            cost=500.00,
        )

        # URL for cancel_trip
        self.cancel_trip_url = reverse(
            'cancel_trip',
            kwargs={'trip_id': self.upcoming_trip.id}
        )
        self.past_trip_url = reverse(
            'cancel_trip',
            kwargs={'trip_id': self.past_trip.id}
        )

    def test_cancel_trip_renders_correctly(self):
        """Test the cancel_trip view renders the correct template."""
        response = self.client.get(self.cancel_trip_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'trips/cancel_trip.html')

    def test_cancel_trip_redirects_if_ineligible(self):
        """Test the view redirects if the trip cannot be canceled."""
        response = self.client.get(self.past_trip_url)
        self.assertRedirects(response, reverse('trips_user'))
        messages = list(response.wsgi_request._messages)
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]),
            "You cannot cancel a trip that has already started."
        )


class CancelTripSuccessViewTest(TestCase):
    '''Tests for the cancel trip success view'''
    def setUp(self):
        '''Set up for the cancel trip success view'''
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.url = reverse('cancel_trip_success')

    def test_redirect_if_not_logged_in(self):
        '''Test login requirement'''
        response = self.client.get(self.url)
        self.assertNotEqual(response.status_code, 200)

    def test_renders_template_for_logged_in_user(self):
        '''Test correct template renders'''
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'trips/cancel_trip_success.html')


class TripsSuperuserViewTest(TestCase):
    '''Test the trips superuser view'''
    def setUp(self):
        '''Set up to test the trips superuser view'''
        # Create a staff user
        self.staff_user = User.objects.create_user(
            username='staffuser',
            password='password',
            is_staff=True
        )
        # Create a non-staff user
        self.non_staff_user = User.objects.create_user(
            username='regularuser',
            password='password'
        )
        self.user_profile = UserProfile.objects.get(user=self.non_staff_user)
        # Create some Trip objects to load
        self.room = Room.objects.create(
            name="new_room",
            sanitised_name="New Room",
            amenities=[1, 2],
            description="A new room description",
            price=10.00,
        )
        # Create instances for testing:
        today = now().date()
        self.trip1 = Trip.objects.create(
            profile=self.user_profile,
            room=self.room,
            start_date=today + timedelta(days=1),
            end_date=today + timedelta(days=2),
            adults=2,
            cost=10.00,
        )
        self.trip2 = Trip.objects.create(
            profile=self.user_profile,
            room=self.room,
            start_date=today - timedelta(days=2),
            end_date=today - timedelta(days=1),
            adults=2,
            cost=10.00,
        )

        # URL for the view
        self.url = reverse('trips_superuser')

    def test_redirect_if_not_logged_in(self):
        '''Check login requirement'''
        # Ensure the view redirects to the login page if not logged in
        response = self.client.get(self.url)
        self.assertNotEqual(response.status_code, 200)

    def test_redirect_if_not_staff(self):
        '''Check staff requirement'''
        # Log in as a non-staff user
        self.client.login(username='regularuser', password='password')

        # Try accessing the view
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

    def test_renders_template_and_context_for_staff(self):
        '''Test with staff'''
        self.client.login(username='staffuser', password='password')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'trips/trips_superuser.html')

        # Check context data
        self.assertIn('trips', response.context)
        self.assertQuerySetEqual(
            response.context['trips'],
            Trip.objects.all().order_by('id')
        )
