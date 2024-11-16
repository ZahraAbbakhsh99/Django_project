from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'total_price', 'status',
                    'status', 'order_date']
    list_filter = ['id', 'status', 'order_date']
    search_fields = ('user__username', 'shipping_address')


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'unit_price', 'total_price']
    search_fields = ('product__name',)
