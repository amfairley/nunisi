from django.contrib import admin
from .models import Room, Amenities


class RoomAdmin(admin.ModelAdmin):
    '''Display options for the room instances in Dhango admin'''
    list_display = (
        'id',
        'name',
        'sanitised_name',
        'amenities',
        'description',
        'image_url',
        'image',
        'price',
        'unavailability'
    )

    ordering = ('id',)


class AmenitiesAdmin(admin.ModelAdmin):
    '''Display options for the amenities instances in Dhango admin'''
    list_display = (
        'id',
        'name',
        'sanitised_name',
        'icon'
    )

    ordering = ('id',)


# Register your models here.
admin.site.register(Room, RoomAdmin)
admin.site.register(Amenities, AmenitiesAdmin)
