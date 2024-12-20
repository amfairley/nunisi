from django.test import TestCase
from .models import Review
from django.apps import apps
from django.db.models import (
    BooleanField,
    ForeignKey,
    TextField,
    PositiveSmallIntegerField,
)
from django.core.exceptions import ValidationError


class ReviewModelTest(TestCase):
    '''Test the Review model'''
    def test_review_model_exists(self):
        '''Check that the app is installed and model defined'''
        self.assertTrue(apps.is_installed('reviews'))
        self.assertIn(
            'Review', [model.__name__ for model in apps.get_models()]
        )

    def test_tirp_field(self):
        '''Test the trip field'''
        # Get the 'trip' field from the model
        field = Review._meta.get_field('trip')
        # Check that the field is a ForeignKey
        self.assertIsInstance(field, ForeignKey)
        self.assertEqual(field.get_internal_type(), 'ForeignKey')
        # Check null status
        self.assertTrue(field.null)
        # Check blank status
        self.assertTrue(field.blank)

    def test_content_field(self):
        '''Test the content field'''
        # Get the 'content' field from the model
        field = Review._meta.get_field('content')
        # Check that the field is a TextField
        self.assertIsInstance(field, TextField)
        self.assertEqual(field.get_internal_type(), 'TextField')
        # Check null status
        self.assertFalse(field.null)
        # Check blank status
        self.assertFalse(field.blank)

    def test_rating_field(self):
        '''Test the rating field'''
        # Get the 'rating' field from the model
        field = Review._meta.get_field('rating')
        # Check that the field is a PositiveSmallIntegerField
        self.assertIsInstance(field, PositiveSmallIntegerField)
        self.assertEqual(
            field.get_internal_type(),
            'PositiveSmallIntegerField'
        )
        # Check null status
        self.assertFalse(field.null)
        # Check blank status
        self.assertFalse(field.blank)

    def test_valid_rating(self):
        """Test that ratings within the range 1-5 are valid."""
        review = Review(content="Valid rating", rating=3)
        try:
            review.full_clean()
        except ValidationError:
            self.fail("ValidationError raised for a valid rating of 3.")

    def test_minimum_rating(self):
        """Test that a rating below 1 raises a ValidationError."""
        review = Review(content="Too low rating", rating=0)
        with self.assertRaises(ValidationError):
            review.full_clean()

    def test_maximum_rating(self):
        """Test that a rating above 5 raises a ValidationError."""
        review = Review(content="Too high rating", rating=6)
        with self.assertRaises(ValidationError):
            review.full_clean()

    def test_verified_field(self):
        '''Test the verified field'''
        # Get the 'verified' field from the model
        field = Review._meta.get_field('verified')
        # Check that the field is a BooleanField
        self.assertIsInstance(field, BooleanField)
        self.assertEqual(field.get_internal_type(), 'BooleanField')
        # Check null status
        self.assertFalse(field.null)
        # Check blank status
        self.assertFalse(field.blank)
        # Check default value
        self.assertEqual(field.default, False)
