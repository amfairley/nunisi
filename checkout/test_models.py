from django.test import TestCase
from django.apps import apps
from .models import Order


class RoomModelTest(TestCase):
    '''Tests for the Room model'''
    def test_moodel_exists(self):
        '''Check that the app is installed and model defined'''
        self.assertTrue(apps.is_installed('checkout'))
        self.assertIn(
            'Order', [model.__name__ for model in apps.get_models()]
        )
