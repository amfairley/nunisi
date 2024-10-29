from django.contrib import admin
from .models import Room, Amenities


class RoomAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'sanitised_name',
        'amenities',
        'description',
        'image_url',
        'image',
        'price',
        'unavailability'
    )

    ordering = ('name',)


class AmenitiesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'sanitised_name',
        'icon'
    )

    ordering = ('name',)


# Register your models here.
admin.site.register(Room, RoomAdmin)
admin.site.register(Amenities, AmenitiesAdmin)
