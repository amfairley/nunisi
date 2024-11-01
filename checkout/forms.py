from django import forms


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
    country = forms.CharField(
        max_length=40,
        required=True,
        label="Country"
    )
    postcode = forms.CharField(
        max_length=20,
        required=False,
        label="Postcode"
    )
    town_or_city = forms.CharField(
        max_length=40,
        required=True,
        label="Town or City"
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
    county = forms.CharField(
        max_length=80,
        required=False,
        label="County"
    )
