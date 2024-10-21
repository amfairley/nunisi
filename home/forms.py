from django import forms


class BookingForm(forms.Form):
    name = forms.CharField()
