from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.card_view, name='cart'),
    path('checkout/', views.checkout_view, name='checkout'),

]