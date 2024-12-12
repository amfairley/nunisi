from django.forms import ModelForm
from .models import Room
from django import forms
from datetime import datetime


class EditRoomForm(ModelForm):
    '''Form to edit a room.'''
    unavailability_input = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Enter dates as YYYY-MM-DD, separated by commas'
            }
        ),
        required=False,
    )

    class Meta:
        '''Meta class for the edit room form'''
        model = Room
        fields = [
            'name', 'sanitised_name', 'amenities', 'description',
            'image', 'price'
        ]

    def clean_unavailability_input(self):
        '''Convert the input dates to usable format'''
        input_data = self.cleaned_data['unavailability_input']
        if not input_data:
            return []
        dates = [date.strip() for date in input_data.split(',')]
        # Validate date format
        for date in dates:
            try:
                # Convert to correct date format
                datetime.strptime(date, '%Y-%m-%d')
            except ValueError:
                raise forms.ValidationError(
                    f"Invalid date format: {date}. Use YYYY-MM-DD."
                )
        return dates

    def save(self, commit=True):
        '''Overwrite the save to include the cleaned unavailable dates'''
        room = super().save(commit=False)
        # Save the cleaned list of dates into the 'unavailability' model field
        room.unavailability = self.cleaned_data['unavailability_input']
        if commit:
            room.save()
        return room
