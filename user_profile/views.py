from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile
from allauth.account.models import EmailAddress
from .forms import EditProfileForm
from django.contrib import messages


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
            messages.success(
                request,
                "Account updated."
            )
            return render(request, 'user_profile/user_profile.html', context)

    else:
        form = EditProfileForm(instance=user_profile)
    context = {
        'user_profile': user_profile,
        'form': form,
    }
    return render(request, 'user_profile/edit_profile.html', context)


def delete_user(request, user_id):
    '''Delete user account functionality'''
    if request.method == 'POST':
        user = request.user
        user.delete()
        messages.success(
            request,
            "Account deleted."
        )
        return redirect('delete_successful')

    # Show the confirm delete page
    return render(request, 'user_profile/delete_user.html')


def delete_successful(request):
    '''Display account deletion success page'''
    return render(request, 'user_profile/delete_successful.html')
