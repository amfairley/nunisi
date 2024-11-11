from django.contrib import admin
from . models import UserProfile, Trip


class UserProfileAdmin(admin.ModelAdmin):
    readonly_fields = (
        'user',
    )

    list_display = (
        'user',
        'full_name',
        'phone_number',
        'country',
        'postcode',
        'town_or_city',
        'street_address1',
        'street_address2',
        'county',
        'newsletter'
    )

    ordering = ('user',)


class TripAdmin(admin.ModelAdmin):
    list_display = (
        'profile',
        'room',
        'start_date',
        'end_date',
        'adults',
        'children',
        'cost',
        'cancelled',
    )

    ordering = ('profile',)


# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Trip, TripAdmin)
