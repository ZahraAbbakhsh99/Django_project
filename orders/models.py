from django.db import models
from products.models import Product
from users.models import User


# Create your models here.
ORDER_STATUS_CHOICES = [('PENDING', 'pending'), ('PAID', 'paid'), ('SHIPPED', 'shipped')]


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='Order', verbose_name='user')
    status = models.CharField(max_length=10, choices=ORDER_STATUS_CHOICES,
                              default='PENDING', verbose_name='status')
    order_date = models.DateTimeField(auto_now_add=True, verbose_name='order_date')
    shipping_address = models.TextField(verbose_name='shipping_address')

    def __str__(self):
        return f"Order{self.id}_{self.user.username}"

    @property
    def total_price(self):
        return sum(item.unit_price for item in self.OrderItem.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,
                              related_name='OrderItem', verbose_name='order')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='OrderItem', verbose_name='product', null=True)
    quantity = models.PositiveIntegerField(null=True, verbose_name='quantity')
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='unit_price', null=True)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order {self.order.id}"

    @property
    def total(self):
        return self.quantity * self.product.price
