from django.forms import ModelForm
from .models import Review
from django.core.exceptions import ValidationError
from django import forms
from django.utils import timezone


class EditReviewForm(ModelForm):
    '''Form to and or edit a review.'''
    rating = forms.ChoiceField(
        choices=[(i, str(i)) for i in range(1, 6)],
        widget=forms.RadioSelect(attrs={'class': 'review-rating'}),
        label="Rating"
    )

    class Meta:
        '''Meta class for the edit room form'''
        model = Review
        fields = [
            'content', 'rating'
        ]
        labels = {
            'content': 'Review content',
        }
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'no-resize-textarea',
                'style': 'resize: none;',
                'placeholder': 'Please describe your experience with us.'
            }),
        }

        # Form validation
        def clean_content(self):
            '''Checks that the content is 10 characters or longer'''
            content = self.cleaned_data.get('content')
            if len(content) < 10:
                raise ValidationError(
                    "Your review must be at least 10 characters long."
                )
            return content

        def clean_rating(self):
            '''Checks that the rating is from 1-5'''
            rating = self.cleaned_data.get('rating')
            if rating not in ['1', '2', '3', '4', '5']:
                raise ValidationError(
                    "Invalid rating. Please select a rating between 1 and 5."
                )
            return rating

        def clean(self):
            '''
            Checks that there is both a rating and content
            and that the trip is in the past
            '''
            cleaned_data = super().clean()
            content = cleaned_data.get('content')
            rating = cleaned_data.get('rating')
            trip = cleaned_data.get('trip')

            # Check that content is supplied
            if rating and not content:
                self.add_error(
                    'content',
                    'Review content is required when a rating is given.'
                )

            # Check if the trip is in the past
            if trip and trip.end_date > timezone.now():
                self.add_error(
                    'trip',
                    'The trip must be in the past to leave a review.'
                )

            return cleaned_data
