import datetime
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .extras import generate_order_id
from .models import OrderItem, Order
from orders.models import MenuItem
from users.models import Profile


def get_user_pending_order(request):
    user = request.user
    user_id = user.id
    user_profile = get_object_or_404(User, id=user_id)
    order = Order.objects.filter(customer=user_profile)
    if order.exists():
        return order[0]
    return 0

@login_required
def add_to_cart(request, item_id):
    user = request.user
    user_id = user.id
    user_profile = get_object_or_404(User, id=user_id)
    item = get_object_or_404(MenuItem, pk=item_id)
    order_item, status = OrderItem.objects.get_or_create(item=item)
    user_order, status = Order.objects.get_or_create(customer=user_profile)
    user_order.items.add(order_item)
    if status:
        user_order.ref_code = generate_order_id()
        user_order.save()
    item_name = item.name
    item_price = item.price
    messages.success(request, 'Item successfully added to your order.')
    messages.success(request, item_name + " price: " + str(item_price))
    return redirect(reverse('orders:index'))

@login_required()
def delete_from_cart(request, item_id):
    item_to_delete = OrderItem.objects.filter(pk=item_id)
    if item_to_delete.exists():
        item_to_delete[0].delete()
        messages.success(request, 'Item successfully removed.')
    return redirect(reverse('cart:order_details'))

@login_required()
def order_details(request, **kwargs):
    existing_order = get_user_pending_order(request)
    context = {
        'order': existing_order
    }
    return render(request, 'cart/order_summary.html', context)

@login_required()
def checkout(request, order_id):
    existing_order = get_user_pending_order(request)
    context = {
        'order': existing_order
    }
    return render(request, 'cart/checkout.html', context)
