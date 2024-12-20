from django.urls import path
from . import views


urlpatterns = [
    path('trips/', views.trips_user, name="trips_user"),
    path('cancel/<int:trip_id>/', views.cancel_trip, name='cancel_trip'),
    path(
        'cancel/<int:trip_id>/send-email/',
        views.send_cancellation_email,
        name='send_cancellation_email'
    ),
    path('trips_superuser/', views.trips_superuser, name="trips_superuser"),
    path(
        'trips_superuser/toggle/<int:trip_id>/',
        views.toggle_trip_status,
        name='toggle_trip_status'
    ),
    path(
        'cancel/success/',
        views.cancel_trip_success,
        name='cancel_trip_success'
    ),
]
