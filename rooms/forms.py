from django.forms import ModelForm
from .models import Room


class EditRoomForm(ModelForm):
    '''Form to edit a room.'''
    class Meta:
        model = Room
        fields = [
            'name', 'sanitised_name', 'amenities', 'description', 'image_url',
            'image', 'price', 'unavailability'
        ]
