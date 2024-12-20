from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from reviews.models import Review
from trips.models import Trip
from user_profile.models import UserProfile
from rooms.models import Room
from datetime import date, timedelta


class AddReviewViewTests(TestCase):
    """Tests for the add_review view."""

    def setUp(self):
        # Create a user and log them in
        self.user = User.objects.create_user(
            username="testuser",
            password="password123"
        )
        self.client = Client()
        self.client.login(username="testuser", password="password123")
        self.user_profile = UserProfile.objects.get(user=self.user)
        # Create instances for testing
        self.room = Room.objects.create(
            name="new_room",
            sanitised_name="New Room",
            amenities=[1, 2],
            description="A new room description",
            price=10.00,
        )
        self.trip = Trip.objects.create(
            profile=self.user_profile,
            room=self.room,
            start_date=date.today(),
            end_date=date.today() + timedelta(days=1),
            adults=2,
            cost=10.00,
        )
        # URL for the add_review view
        self.url = reverse('add_review', kwargs={'trip_id': self.trip.id})

    def test_add_review_renders_correctly(self):
        """Test that the add_review view renders correctly."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/add_review.html')

    def test_add_review_valid_functionality(self):
        """Test that a valid form submission creates a review."""
        data = {
            'content': 'Great stay!',
            'rating': 5
        }
        response = self.client.post(self.url, data)
        # Expect the page to redirect
        self.assertEqual(response.status_code, 302)
        # Check a review is created
        self.assertEqual(Review.objects.count(), 1)
        review = Review.objects.first()
        # Check the review content
        self.assertEqual(review.content, 'Great stay!')
        self.assertEqual(review.rating, 5)
        self.assertEqual(review.trip, self.trip)

    def test_add_review_invalid_functionality(self):
        """Test that an invalid form submission does not create a review."""
        data = {
            'content': '',
            'rating': 10
        }
        response = self.client.post(self.url, data)
        # Check for no redirection
        self.assertEqual(response.status_code, 200)
        # Check for no reviews
        self.assertEqual(Review.objects.count(), 0)
        # Check the error message
        self.assertContains(
            response,
            "Please correct the errors listed below the form."
        )

    def test_redirects_for_unauthenticated_user(self):
        """Test that an unauthenticated user cannot leave a review"""
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)


class EditReviewViewTests(TestCase):
    """Tests for the edit_review view."""

    def setUp(self):
        # Create a user and log them in
        self.user = User.objects.create_user(
            username="testuser",
            password="password123"
        )
        self.client = Client()
        self.client.login(username="testuser", password="password123")
        self.user_profile = UserProfile.objects.get(user=self.user)
        # Create instances for testing
        self.room = Room.objects.create(
            name="new_room",
            sanitised_name="New Room",
            amenities=[1, 2],
            description="A new room description",
            price=10.00,
        )
        self.trip = Trip.objects.create(
            profile=self.user_profile,
            room=self.room,
            start_date=date.today(),
            end_date=date.today() + timedelta(days=1),
            adults=2,
            cost=10.00,
        )
        self.review = Review.objects.create(
            trip=self.trip,
            content="test review",
            rating=3,
        )
        # URL for the add_review view
        self.url = reverse('edit_review', kwargs={'review_id': self.review.id})

    def test_edit_review_renders_correctly(self):
        """Test that the edit_review view renders correctly."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/edit_review.html')

    def test_edit_review_valid_functionality(self):
        """Test that a valid form submission updates the review."""
        data = {
            'content': 'updated review',
            'rating': 5
        }
        response = self.client.post(self.url, data)
        # Expect the page to redirect
        self.assertEqual(response.status_code, 302)
        # Check there is still only 1 review
        self.assertEqual(Review.objects.count(), 1)
        review = Review.objects.first()
        # Check the review content
        self.assertEqual(review.content, 'updated review')
        self.assertEqual(review.rating, 5)
        self.assertEqual(review.trip, self.trip)

    def test_edit_review_invalid_functionality(self):
        """Test that an invalid form submission does not update the review."""
        data = {
            'content': '',
            'rating': 10
        }
        response = self.client.post(self.url, data)
        # Check for no redirection
        self.assertEqual(response.status_code, 200)
        # Check for still only one review
        self.assertEqual(Review.objects.count(), 1)
        review = Review.objects.first()
        # Check the review content
        self.assertEqual(review.content, 'test review')
        self.assertEqual(review.rating, 3)
        self.assertEqual(review.trip, self.trip)
        # Check the error message
        self.assertContains(
            response,
            "Please correct the errors listed below the form."
        )

    def test_redirects_for_unauthenticated_user(self):
        """Test that an unauthenticated user cannot edit a review"""
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)


class DeleteReviewViewTests(TestCase):
    """Tests for the delete_review view."""

    def setUp(self):
        # Create a user and log them in
        self.user = User.objects.create_user(
            username="testuser",
            password="password123"
        )
        self.client = Client()
        self.client.login(username="testuser", password="password123")
        self.user_profile = UserProfile.objects.get(user=self.user)
        # Create instances for testing
        self.room = Room.objects.create(
            name="new_room",
            sanitised_name="New Room",
            amenities=[1, 2],
            description="A new room description",
            price=10.00,
        )
        self.trip = Trip.objects.create(
            profile=self.user_profile,
            room=self.room,
            start_date=date.today(),
            end_date=date.today() + timedelta(days=1),
            adults=2,
            cost=10.00,
        )
        self.review = Review.objects.create(
            trip=self.trip,
            content="test review",
            rating=3,
        )
        # URL for the add_review view
        self.url = reverse(
            'delete_review',
            kwargs={'review_id': self.review.id}
        )

    def test_redirect_after_deletion(self):
        """Test that the user is redirected to trips_user after deletion."""
        response = self.client.post(self.url)
        self.assertRedirects(response, reverse('trips_user'))

    def test_delete_review_invalid_request(self):
        """Test that a GET request does not delete the review."""
        response = self.client.get(self.url)
        # Check for redirection
        self.assertEqual(response.status_code, 302)
        # Check the review still existis
        self.assertEqual(Review.objects.count(), 1)

    def test_delete_review_invalid_id(self):
        """Test that a 404 is raised for an invalid review ID."""
        invalid_url = reverse('delete_review', kwargs={'review_id': 9999})
        response = self.client.post(invalid_url)
        self.assertEqual(response.status_code, 404)
