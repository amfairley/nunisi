from django.http import HttpResponseRedirect, Http404
from django.shortcuts import redirect


def go_back_or_404(request):
    '''
    View for diverting the user back a page using the back button
    '''
    # Get the referer
    referer = request.META.get('HTTP_REFERER')
    # Get current url
    current_url = request.build_absolute_uri()
    if referer:
        # If referer bug get it from GET
        if referer == current_url:
            referer = request.GET.get('referer')
            if referer:
                return redirect(referer)
        else:
            return HttpResponseRedirect(referer)
    else:
        raise Http404("No previous page found.")
