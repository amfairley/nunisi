from django.urls import path
from .views import go_back_or_404

urlpatterns = [
    path('go-back/', go_back_or_404, name='go_back')
]
