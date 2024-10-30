from django.urls import path
from . import views


urlpatterns = [
    path('', views.available_rooms, name="available_rooms")
]
