from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from products.models import Product
from users.models import User
from .models import *
from .forms import *


# Create your views here.
@login_required()
def card_view(request, user_id):
    user = User.objects.get(id=user_id)
    order = Order.objects.get(user=user, status='PENDING')
    items = OrderItem.objects.filter(order=order)
    is_empty = True if items.count() == 0 else False

    return render(request, 'Card.html', {"items": items, "order": order, "is_empty": is_empty})


@login_required()
def add_to_card(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    order = Order.objects.get(user=request.user, status='PENDING')
    order.save()
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)
    if created:
        order_item.quantity = 1
        order_item.unit_price = product.price
    else:
        if order_item.quantity < product.stock-1:
            order_item.quantity += 1
        else:
            messages.error(request, 'There is not enough product stock.')
            return redirect('productdetail', pk=product_id)
    order_item.save()
    messages.success(request, 'The product has been added to your cart')
    return redirect('cart', user_id=request.user.id)


@login_required()
def remove_from_cart(request, order_id, item_id):
    order = Order.objects.get(id=order_id)
    item = get_object_or_404(OrderItem, id=item_id, order=order)
    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()
    return redirect('cart', user_id=request.user.id)


@login_required()
def checkout_view(request, user_id):
    order = Order.objects.filter(user=request.user, status='PENDING').first()
    if not order or not order.items.exists():
        messages.error(request, 'Your shopping cart is empty')
        return redirect('cart')
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.cleaned_data['address']
            order.address = address
            order.status = 'PENDING'
            order.save()
            messages.success(request, 'Your order has been registered. Please go to the payment page.')
            return redirect('orderconfirmation', order_id=order.id)
    else:
        form = forms.AdderssForm()
    return render(request, 'CheckOut.html', {'form': form, 'order': order})


@login_required()
def user_order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('created_at')
    return render(request, 'OrderHistoryView.html', {'orders': orders})


@login_required()
def confirm_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    if order.status == 'PENDING':
        order.status = 'PAID'
        order.save()
    else:
        return redirect('cart')

    return render(request, 'OrderConfirmationView.html', {'order': order})



