from django import forms


class BookingForm(forms.Form):
    check_in_date = forms.DateField(
        widget=forms.DateInput(
            attrs={'type': 'date', 'class': 'form-control'}
        ),
        label='Check-in date',
        required=True
    )
    check_out_date = forms.DateField(
        required=True
    )
