from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from trips.models import Trip
from .models import Review
from .forms import EditReviewForm
from django.contrib import messages
from django.core.mail import send_mail


# Create your views here.
@login_required
def add_review(request, trip_id):
    '''View to enter details and add a new review'''
    form = EditReviewForm()

    # Get the trip
    trip = get_object_or_404(Trip, id=trip_id)

    # If the form is submitted
    if request.method == 'POST':
        form = EditReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.trip = trip
            review.save()

            # Email to let website owner verify review
            recipient_email = "adamfairley1990@gmail.com"
            subject = f"Review Submitted for Trip #{trip.id}"
            message = f"""
            Dear Team,

            A review has been submitted:
            - Review content: {review.content}
            - Review Rating: {review.rating}

            Please review this review and verify it.
            """
            try:
                send_mail(
                    subject,
                    message,
                    # From email
                    'adamfairley1990@gmail.com',
                    [recipient_email],
                    fail_silently=False,
                )
                messages.success(
                    request,
                    "The hotel owner has been notified of your review."
                )
            except Exception as e:
                messages.error(
                    request,
                    f"An error occurred while sending the email: {e}"
                )

            # Redirect to trips page
            messages.success(
                request,
                "Review added."
            )
            return redirect('trips_user')
        else:
            messages.error(
                request,
                "Please correct the errors listed below the form."
            )

    context = {
        'form': form,
        'trip': trip,
    }
    return render(request, 'reviews/add_review.html', context)


# Create your views here.
@login_required
def edit_review(request, review_id):
    '''View to enter details and add a new review'''
    review = get_object_or_404(Review, id=review_id)
    trip = review.trip
    form = EditReviewForm(instance=review)

    # If the form is submitted
    if request.method == 'POST':
        form = EditReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            # Update verfied status
            review.verified = False
            review.save()
            # Email to let website owner verify updated review
            recipient_email = "adamfairley1990@gmail.com"
            subject = f"Review Update Submitted for Trip #{trip.id}"
            message = f"""
            Dear Team,

            An update to a review has been submitted:
            - Review content: {review.content}
            - Review Rating: {review.rating}

            Please review this review and verify it.
            """
            try:
                send_mail(
                    subject,
                    message,
                    # From email
                    'adamfairley1990@gmail.com',
                    [recipient_email],
                    fail_silently=False,
                )
                messages.success(
                    request,
                    "The hotel owner has been notified of your review update."
                )
            except Exception as e:
                messages.error(
                    request,
                    f"An error occurred while sending the email: {e}"
                )

            # Redirect to trips page
            messages.success(
                request,
                "Review updated."
            )
            return redirect('trips_user')
        else:
            messages.error(
                request,
                "Please correct the errors listed below the form."
            )

    context = {
        'form': form,
        'review': review,
    }
    return render(request, 'reviews/edit_review.html', context)


@login_required
def delete_review(request, review_id):
    """View to delete a review"""
    review = get_object_or_404(Review, id=review_id)

    if request.method == "POST":
        review.delete()
        messages.success(request, "Review deleted successfully.")
        return redirect('trips_user')

    # Handle non-post
    messages.error(request, "Invalid request.")
    return redirect('trips_user')
