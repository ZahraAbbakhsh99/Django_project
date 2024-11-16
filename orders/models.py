from django.db import models
from products.models import Product
from users.models import User


# Create your models here.
ORDER_STATUS_CHOICES = [('PENDING', 'PENDING'), ('PAID', 'PAID'), ('SHIPPED', 'SHIPPED')]


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='Order', verbose_name='user')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='total_price')
    status = models.CharField(max_length=10, choices=ORDER_STATUS_CHOICES,
                              default='PENDING', verbose_name='status')
    order_date = models.DateTimeField(auto_now_add=True, verbose_name='order_date')
    shipping_address = models.TextField(verbose_name='shipping_address')

    def __str__(self):
        return f"Order{self.id}_{self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,
                              related_name='OrderItem', verbose_name='order')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='OrderItem', verbose_name='product')
    quantity = models.PositiveIntegerField(default=1, verbose_name='quantity')
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='unit_price')

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    @property
    def total_price(self):
        return self.quantity * self.unit_price
