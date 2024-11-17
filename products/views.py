from django.shortcuts import render, get_object_or_404
from .models import *


# Create your views here.
def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'ProductDetail.html', {'product': product})


def category_view(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    products = Product.objects.filter(category=category)
    return render(request, 'CategoryView.html', {'category': category, 'products': products})

