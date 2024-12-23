from django.http import HttpResponseRedirect, Http404
from django.shortcuts import redirect


def go_back_or_404(request):
    '''
    View for diverting the user back a page using the back button
    '''
    referer = request.GET.get('referer')
    if referer:
        return redirect(referer)
    else:
        raise Http404("No previous page found.")
