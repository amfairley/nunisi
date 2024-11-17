from django.db import models
from django.contrib.auth.models import User
from rooms.models import Room
from django_countries.fields import CountryField


class UserProfile(models.Model):
    '''
    A user profile model for default delivery information
    and newsletter signup
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, null=True, blank=True)
    full_name = models.CharField(max_length=150, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    country = CountryField(blank_label='Country *', null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=True, blank=True)
    street_address1 = models.CharField(max_length=80, null=True, blank=True)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    newsletter = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Trip(models.Model):
    profile = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    room = models.ForeignKey(
        Room,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=False, blank=False)
    adults = models.IntegerField(null=False, blank=False)
    children = models.IntegerField(default=0)
    infants = models.IntegerField(default=0)
    cost = models.DecimalField(null=False, max_digits=10, decimal_places=2)
    cancelled = models.BooleanField(default=False)
