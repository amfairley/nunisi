from django.db import models
from trips.models import Trip
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):
    '''Review model'''
    trip = models.ForeignKey(
        Trip,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    content = models.TextField(null=False, blank=False)
    rating = models.PositiveSmallIntegerField(
        null=False,
        blank=False,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    verified = models.BooleanField(null=False, blank=False, default=False)
