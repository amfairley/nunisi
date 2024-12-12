from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=254, null=False, blank=False)
    sanitised_name = models.CharField(max_length=254, null=False, blank=False)
    amenities = models.JSONField(default=list, null=False, blank=False)
    description = models.TextField(
        default='Room Description',
    )
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        blank=False
    )
    unavailability = models.JSONField(default=list, null=False, blank=True)

    def __str__(self):
        return self.name

    def get_sanitised_name(self):
        return self.sanitised_name


class Amenities(models.Model):
    class Meta:
        verbose_name_plural = 'Amenities'
    name = models.CharField(max_length=50)
    sanitised_name = models.CharField(max_length=100, default="Amenity Name")
    icon = models.CharField(max_length=150, default="Font Awesome Icon")

    def __str__(self):
        return self.name
