from django.shortcuts import render

# Create your views here.


def user_profile(request):
    ''' Display the user's profile '''
    template = 'user_profile/user_profile.html'
    context = {}
    return render(request, template, context)
