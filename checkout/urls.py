from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('checkout/success/', views.checkout, name='payment'),
    path(
        'cache_checkout_data/',
        views.cache_checkout_data,
        name='cache_checkout_data'
    ),
    path('wh/', webhook, name='webhook'),
]
