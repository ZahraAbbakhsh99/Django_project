from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.card_view, name='cart'),
    path('removeitem/', views.remove_from_cart, name='removeitem'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('addtocard/<int:product_id>/', views.add_to_card, name='add_to_card'),
    path('orderhistory/', views.user_order_history, name='user_order_history'),
    path('orderconfirmation/', views.confirm_order, name='confirm_order'),
]