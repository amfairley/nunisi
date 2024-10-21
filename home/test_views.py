from django.test import TestCase


class TestHomeView(TestCase):
    '''A class to test the home views'''
    def test_view_works(self):
        '''A test to check that the correct template is used and page loads'''
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
