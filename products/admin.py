from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_category')
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'stock', 'category', 'created_at', 'image')
    list_filter = ('name', 'price', 'stock', 'category', 'created_at')
    search_fields = ('name', 'category', 'description')
