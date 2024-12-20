from django.urls import path
from . import views


urlpatterns = [
    path(
        'edit_review/<int:review_id>/',
        views.edit_review,
        name="edit_review"
    ),
    path('add/<int:trip_id>/', views.add_review, name='add_review'),
    path('delete/<int:review_id>/', views.delete_review, name='delete_review'),
]
