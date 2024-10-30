from django.shortcuts import render


def checkout(request):
    '''A view to return the checkout'''
    return render(request, 'checkout/checkout.html')
