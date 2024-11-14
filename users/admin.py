from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *


# Register your models here.
class UserAdmin(BaseUserAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_admin', 'is_customer']
    list_filter = ['username', 'email']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    ordering = ('username',)


admin.register(User, UserAdmin)
