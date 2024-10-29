from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=254)
    sanitised_name = models.CharField(max_length=254)
    amenities = models.JSONField(default=list)
