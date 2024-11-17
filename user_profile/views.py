from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile, Trip
from allauth.account.models import EmailAddress
from rooms.models import Amenities
from .forms import EditProfileForm
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.


def user_profile(request):
    ''' Display the user's profile '''
    # Get the profile from the current user
    user = request.user
    user_profile = get_object_or_404(UserProfile, user=request.user)
    email_addresses = EmailAddress.objects.filter(user=request.user)
    context = {
        'user_profile': user_profile,
        'email_addresses': email_addresses,
        'user': user,
    }
    return render(request, 'user_profile/user_profile.html', context)


def edit_profile(request):
    '''Divert user to the edit_profile page'''
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.POST:
        form = EditProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            email_addresses = EmailAddress.objects.filter(user=request.user)
            context = {
                'user_profile': user_profile,
                'email_addresses': email_addresses,
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
    # Get amenities
    amenities = Amenities.objects.all()

    context = {
        'user_profile': user_profile,
        'trips': trips,
        'amenities': amenities,
    }
    return render(request, 'user_profile/trips.html', context)


@staff_member_required
def trips_superuser(request):
    '''Display all the trips for the admin'''
    trips = Trip.objects.all()

    context = {
        'trips': trips,
    }
    return render(request, 'user_profile/trips_superuser.html', context)


def delete_user(request, user_id):
    '''Delete user account functionality'''
    if request.method == 'POST':
        user = request.user
        user.delete()
        return redirect('delete_successful')  # Redirect to success page

    # Show the confirm delete page
    return render(request, 'user_profile/delete_user.html')


def delete_successful(request):
    '''Display account deletion success page'''
    return render(request, 'user_profile/delete_successful.html')
