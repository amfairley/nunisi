from django.http import HttpResponseRedirect, Http404


def go_back_or_404(request):
    '''
    View for diverting the user back a page using the back button
    '''
    referer = request.META.get('HTTP_REFERER')
    if referer:
        return HttpResponseRedirect(referer)
    else:
        raise Http404("No previous page found.")
