from django.shortcuts import render
from django.conf import settings
from reviews.models import Review


def index(request):
    """A view to return the home page"""
    # Check for any reviews to display
    all_reviews = Review.objects.all()
    # Only get the verified reviews
    reviews = []
    for review in all_reviews:
        if review.verified:
            reviews.append(review)
        else:
            continue

    context = {
        'MEDIA_URL': settings.MEDIA_URL,
        'reviews': reviews,
    }
    return render(request, 'home/index.html', context)
