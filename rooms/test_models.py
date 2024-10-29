from django.test import TestCase
from django.apps import apps
from .models import Room


class RoomModelTest(TestCase):
    '''Tests for the Room model'''
    def test_room_model_exists(self):
        '''Check that the app is installed and model defined'''
        self.assertTrue(apps.is_installed('rooms'))
        self.assertIn(
            'Room', [model.__name__ for model in apps.get_models()]
        )
