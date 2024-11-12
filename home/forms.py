from django import forms
from django.core.exceptions import ValidationError
from datetime import date, timedelta


class BookingForm(forms.Form):
    check_in_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control',
                # Set minimum value of today
                'min': date.today().isoformat(),
                # Set maximum value of +1 year
                'max': (date.today() + timedelta(days=365)).isoformat(),
            }
        ),
        label='Check-in',
        required=True
    )
    check_out_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control',
                # Set minimum value of today + 1
                'min': (date.today() + timedelta(days=1)).isoformat(),
                'max': (date.today() + timedelta(days=365)).isoformat(),
            }
        ),
        label='Check-out',
        required=True
    )
    adults = forms.IntegerField(
        min_value=1,
        max_value=5,
        label="Adults (18+)",
        required=True,
        widget=forms.NumberInput(attrs={
            'onchange': 'updateGuestCount()'
        })
    )
    children = forms.IntegerField(
        min_value=0,
        max_value=5,
        label="Children (5+)",
        required=False,
        widget=forms.NumberInput(attrs={
            'onchange': 'updateGuestCount()'
        })
    )
    infants = forms.IntegerField(
        min_value=0,
        max_value=5,
        label="Infants (0-5)",
        required=False,
        widget=forms.NumberInput(attrs={
            'onchange': 'updateGuestCount()'
        })
    )

    class Meta:
        fields = [
            'check_in_date',
            'check_out_date',
            'adults',
            'children',
            'infants'
        ]

    def clean_check_in_date(self):
        check_in_date = self.cleaned_data['check_in_date']
        if check_in_date < date.today() + timedelta(days=1):
            raise ValidationError("Check-in date must be tomorrow or later.")
        return check_in_date

    def clean_check_out_date(self):
        check_in_date = self.cleaned_data.get('check_in_date')
        check_out_date = self.cleaned_data['check_out_date']

        # Ensure check-out date is after check-in date
        if check_in_date and check_out_date <= check_in_date:
            raise ValidationError(
                "Check-out date must be after the check-in date."
            )
        return check_out_date
