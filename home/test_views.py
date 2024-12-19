from django.test import TestCase
from reviews.models import Review


class TestHomeView(TestCase):
    '''A class to test the home views'''
    def test_view_works(self):
        '''A test to check that the correct template is used and page loads'''
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_reviews_displayed(self):
        '''A test to check that only verified reviews are displayed'''
        # Create some reviews (verified and unverified)
        verified_review = Review.objects.create(
            content="Great product!",
            rating=5,
            verified=True)
        unverified_review = Review.objects.create(
            content="Not bad",
            rating=4,
            verified=False)

        # Request the home page
        response = self.client.get('/')

        # Ensure only verified reviews are displayed
        self.assertContains(response, "Great product!")
        self.assertNotContains(response, "Not bad")
