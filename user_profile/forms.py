from django import forms
from django.forms import ModelForm
from checkout.forms import CheckoutForm
from .models import UserProfile


class EditProfileForm(CheckoutForm, ModelForm):
    '''
    Form to edit the profile.
    Built from CheckoutForm with requirements set to false.
    Email field removed.
    '''
    newsletter = forms.BooleanField(
        required=False,
        label="Newsletter Subscription"
    )

    class Meta:
        model = UserProfile
        fields = [
            'full_name', 'phone_number', 'street_address1', 'street_address2',
            'town_or_city', 'county', 'country', 'newsletter'
        ]

    def __init__(self, *args, **kwargs):
        '''Update the default CheckoutForm requirements'''
        super().__init__(*args, **kwargs)

        # Update field requirements to false
        self.fields['full_name'].required = False
        self.fields['phone_number'].required = False
        self.fields['street_address1'].required = False
        self.fields['town_or_city'].required = False
        self.fields['country'].required = False

        # Remove email field
        self.fields.pop('email', None)
