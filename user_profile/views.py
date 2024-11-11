from django.shortcuts import render, get_object_or_404
from .models import UserProfile, Trip
from .forms import EditProfileForm

# Create your views here.


def user_profile(request):
    ''' Display the user's profile '''
    # Get the profile from the current user
    user_profile = get_object_or_404(UserProfile, user=request.user)
    context = {
        'user_profile': user_profile,
    }
    return render(request, 'user_profile/user_profile.html', context)


def edit_profile(request):
    '''Divert user to the edit_profile page'''
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.POST:
        form = EditProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()

            context = {
                'user_profile': user_profile,
            }
            return render(request, 'user_profile/user_profile.html', context)

    else:
        form = EditProfileForm(instance=user_profile)
    context = {
        'user_profile': user_profile,
        'form': form,
    }
    return render(request, 'user_profile/edit_profile.html', context)


def trips_user(request):
    ''' Display the user's trips '''
    # Get the profile from the current user
    user_profile = get_object_or_404(UserProfile, user=request.user)
    # Get the user's trips
    trips = Trip.objects.filter(profile=user_profile)

    context = {
        'user_profile': user_profile,
        'trips': trips,
    }
    return render(request, 'user_profile/trips.html', context)
