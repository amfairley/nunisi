from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget


class CheckoutForm(forms.Form):
    full_name = forms.CharField(
        max_length=150,
        required=True,
        label="Full Name"
    )
    email = forms.EmailField(
        max_length=254,
        required=True,
        label="Email Address"
    )
    phone_number = forms.CharField(
        max_length=20,
        required=True,
        label="Phone Number"
    )
    street_address1 = forms.CharField(
        max_length=80,
        required=True,
        label="Street Address Line 1"
    )
    street_address2 = forms.CharField(
        max_length=80,
        required=False,
        label="Street Address Line 2"
    )
    town_or_city = forms.CharField(
        max_length=40,
        required=True,
        label="Town or City"
    )
    county = forms.CharField(
        max_length=80,
        required=False,
        label="County"
    )
    postcode = forms.CharField(
        max_length=20,
        required=False,
        label="Postcode"
    )
    country = CountryField(blank_label='Country *').formfield(
        required=True,
        widget=CountrySelectWidget(layout='{widget}'),
        label="Country"
    )
