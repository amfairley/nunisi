from django.shortcuts import render
from django.conf import settings


def index(request):
    """A view to return the home page"""
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(request, 'home/index.html', context)
