from django.shortcuts import render
from products.models import *
from django.db.models import Max, Min


def home_view(request):
    query = request.GET.get('laptop')

    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    price_range = Product.objects.aggregate(Min('price'), Max('price'))
    products = Product.objects.all()

    if query:
        products = Product.filter(name__icontains=query)
    if min_price:
        products = Product.filter(price__get=min_price)
    if max_price:
        products = Product.filter(price__Ite=max_price)

    categories = Category.objects.all()
    featured_products = Product.objects.filter(stock__lt=5).order_by('created_at')[:10]

    context = {
        'products': products,
        'categories': categories,
        'featured_products': featured_products,
        'query': query,
        'price_renge': price_range
    }
    return render(request, 'HomePage.html', context)


def search_result(request):
    return render(request, 'SearchResults.html')