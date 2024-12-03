from django.test import TestCase, RequestFactory
from django.http import Http404
from .views import go_back_or_404


class GoBackOr404ViewTests(TestCase):
    '''Test the back button'''
    def setUp(self):
        '''Set up the test for the back button'''
        self.factory = RequestFactory()

    def test_redirects_to_referer_when_present(self):
        '''Test the working referer'''
        request = self.factory.get('/')
        request.META['HTTP_REFERER'] = '/previous-page/'
        response = go_back_or_404(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], '/previous-page/')

    def test_raises_404_when_referer_missing(self):
        '''Test the 404 functionality'''
        # Create a mock request without an HTTP_REFERER header
        request = self.factory.get('/')

        # Assert the view raises Http404
        with self.assertRaises(Http404):
            go_back_or_404(request)
