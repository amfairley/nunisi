from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=254)
    sanitised_name = models.CharField(max_length=254)
    amenities = models.JSONField(default=list)
    description = models.TextField(
        default='Room Description'
    )
    image_url = models.URLField(max_length=1024, null=True, blank=True)
