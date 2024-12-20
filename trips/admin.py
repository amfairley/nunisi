from django.contrib import admin
from . models import Trip


class TripAdmin(admin.ModelAdmin):
    '''Display the trip instances on the admin page'''
    list_display = (
        'id',
        'profile',
        'room',
        'start_date',
        'end_date',
        'adults',
        'children',
        'cost',
        'cancelled',
    )

    list_editable = ('cancelled',)

    ordering = ('id',)


admin.site.register(Trip, TripAdmin)
