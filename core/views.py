from django.shortcuts import render
from products.models import *


def home_view(request):
    categories = Category.objects.all()
    featured_products = Product.objects.filter(stock__lt=5).order_by('created_at')[:10]

    context = {'categories': categories,
               'featured_products': featured_products}
    return render(request, 'HomePage.html', context)



