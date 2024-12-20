from django.db import models
from django.utils import timezone


# Create your models here.
class Category(models.Model):
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, unique=True, verbose_name="Category name")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='product name')
    description = models.TextField(verbose_name='description', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='price')
    stock = models.PositiveIntegerField(verbose_name='stock')
    image = models.ImageField(upload_to='product_images/', blank=True, null=True, verbose_name='product_image')

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Products', verbose_name='category')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='created_at')

    def __str__(self):
        return f"{self.name}, {self.price}, ma{self.stock}"
