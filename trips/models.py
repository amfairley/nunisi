from django.db import models
from rooms.models import Room
from user_profile.models import UserProfile


class Trip(models.Model):
    '''Trip model'''
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
