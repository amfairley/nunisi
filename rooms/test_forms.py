from django.test import TestCase
from rooms.models import Room
from rooms.forms import EditRoomForm


class EditRoomFormTest(TestCase):
    '''Test the edit room form'''
    def setUp(self):
        '''Create a room to edit'''
        # Create a sample Room object for testing
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

    def test_form_valid_data(self):
        """Test form with valid data"""
        form_data = {
            'name': "updated_room",
            'sanitised_name': "Updated Room",
            'amenities': "[1]",
            'description': "An updated description",
            'price': 120.50,
            'unavailability_input': "2024-12-20, 2024-12-31"
        }
        form = EditRoomForm(data=form_data, instance=self.room)
        self.assertTrue(form.is_valid())

        # Save the form and check that it has been updated correctly
        room = form.save()
        self.assertEqual(room.name, "updated_room")
        self.assertEqual(room.sanitised_name, "Updated Room")
        self.assertEqual(room.amenities, [1])
        self.assertEqual(room.price, 120.50)
        self.assertEqual(room.unavailability, ["2024-12-20", "2024-12-31"])

    def test_form_invalid_date_format(self):
        """Test form with invalid date format in unavailability_input"""
        form_data = {
            'unavailability_input': "2024-12-25, invalid-date"
        }
        form = EditRoomForm(data=form_data, instance=self.room)
        # Check that the form is invalid
        self.assertFalse(form.is_valid())
        # Check there is an error with the unavailability input
        self.assertIn("unavailability_input", form.errors)
        # Confirm the error message
        self.assertEqual(
            form.errors["unavailability_input"],
            ["Invalid date format: invalid-date. Use YYYY-MM-DD."]
        )

    def test_form_missing_required_fields(self):
        """Test form missing required fields"""
        form_data = {
            'name': '',
            'description': '',
            'amenities': [],
            'price': None,
        }
        form = EditRoomForm(data=form_data, instance=self.room)
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)
        self.assertIn("description", form.errors)
        self.assertIn("price", form.errors)
        self.assertIn("amenities", form.errors)
