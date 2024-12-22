from django.shortcuts import render
from products.models import Product, Category


def home_view(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    for category in categories:
        cat_product = Product.objects.filter(category=category)
        if not cat_product.exists():
            ...

    limited_number_of_product = Product.objects.filter(stock__lt=5).order_by('created_at')[:10]

    context = {
        'products': products,
        'categories': categories,
        'limited_number_of_product': limited_number_of_product,
    }
    return render(request, 'HomePage.html', context)


def search_result(request):
    ...
    return render(request, 'SearchResults.html')
