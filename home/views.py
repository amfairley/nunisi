from django.shortcuts import render


def index(request):
    """A view to return the home page"""
    return render(request, 'home/index.html')
