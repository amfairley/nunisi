from django.shortcuts import render, get_object_or_404
from .models import UserProfile

# Create your views here.


def user_profile(request):
    ''' Display the user's profile '''
    # Get the profile from the current user
    user_profile = get_object_or_404(UserProfile, user=request.user)
    template = 'user_profile/user_profile.html'
    context = {
        'user_profile': user_profile,
    }
    return render(request, template, context)
