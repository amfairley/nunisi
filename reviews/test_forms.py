from django.test import TestCase
from .models import Review
from .forms import EditReviewForm


class EditReviewFormTest(TestCase):
    '''Test the edit review form'''
    def setUp(self):
        '''Create a review to edit'''
        # Create a sample Review object for testing
        self.review = Review.objects.create(
            content="test review",
            rating=3,
        )

    def test_form_valid_data(self):
        """Test form with valid data"""
        form_data = {
            'content': "test review update",
            'rating': 2,
        }
        form = EditReviewForm(data=form_data, instance=self.review)
        self.assertTrue(form.is_valid())

        # Save the form and check that it has been updated correctly
        review = form.save()
        self.assertEqual(review.content, "test review update")
        self.assertEqual(review.rating, 2)

    def test_form_missing_required_fields(self):
        """Test form missing required fields"""
        form_data = {
            'content': '',
            'rating': None,
        }
        form = EditReviewForm(data=form_data, instance=self.review)
        self.assertFalse(form.is_valid())
        self.assertIn("content", form.errors)
        self.assertIn("rating", form.errors)
