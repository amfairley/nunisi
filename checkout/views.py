from django.shortcuts import render


def checkout(request):
    '''A view to return the checkout'''
    # Initialise variables
    room_id = None
    total_days = None
    check_in_date = None
    check_out_date = None
    adults = None
    children = None
    infants = None

    if request.POST:
        # Get values from the form
        room_id = request.POST.get('room_id')
        total_days = request.POST.get('total_days')
        check_in_date = request.POST.get('check_in_date')
        check_out_date = request.POST.get('check_out_date')
        adults = request.POST.get('adults')
        children = request.POST.get('children')
        infants = request.POST.get('infants')

    context = {
        'room_id': room_id,
        'total_days': total_days,
        'check_in_date': check_in_date,
        'check_out_date': check_out_date,
        'adults': adults,
        'children': children,
        'infants': infants
    }
    return render(request, 'checkout/checkout.html', context)
