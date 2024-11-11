from django.urls import path
from . import views


urlpatterns = [
    path('', views.user_profile, name="user_profile"),
    path('edit_profile/', views.edit_profile, name="edit_profile"),
    path('trips/', views.trips_user, name="trips_user"),
    path('trips_superuser/', views.trips_superuser, name="trips_superuser"),
]
