from django.contrib import admin
from . models import Review


class ReviewAdmin(admin.ModelAdmin):
    '''Display reviews in the admin'''
    list_display = (
        'id',
        'trip',
        'content',
        'rating',
        'verified',
    )

    list_editable = ('verified',)

    ordering = ('id',)


admin.site.register(Review, ReviewAdmin)
