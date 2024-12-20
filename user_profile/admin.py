from django.contrib import admin
from . models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    '''Display the user profiles in admin'''
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


# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)
