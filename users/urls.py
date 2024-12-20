from django.urls import path
from .views import *


urlpatterns = [
    path('profile/', user_profile, name='user_profile'),
    path('login/', user_login, name='login'),
    path('register/', user_register, name='register'),
    path('editprofile/', edit_user_profile, name='editprofile'),
    path('logout/', user_logout, name='logout'),
]
