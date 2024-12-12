from django.urls import path
from . import views


urlpatterns = [
    path('', views.available_rooms, name="available_rooms"),
    path('rooms_superuser/', views.rooms_superuser, name="rooms_superuser"),
    path('edit_room/<int:room_id>/', views.edit_room, name="edit_room"),
    path('delete_room/<int:room_id>/', views.delete_room, name="delete_room"),
    path('add_room/', views.add_room, name="add_room"),
]
