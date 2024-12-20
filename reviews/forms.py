from django.forms import ModelForm
from .models import Review
from django import forms


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
