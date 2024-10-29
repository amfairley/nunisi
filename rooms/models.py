from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=254)
    sanitised_name = models.CharField(max_length=254)
    amenities = models.JSONField(default=list)
    description = models.TextField(
        default='Room Description'
    )
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
    )
