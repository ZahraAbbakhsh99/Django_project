from django.urls import path
from . import views

urlpatterns = [
    path('productdetail/<int:pk>/', views.product_detail_view, name='productdetail'),
    path('category/<str:category_name>/', views.category_view, name='category'),
]
