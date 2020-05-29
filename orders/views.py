from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import MenuItem, Topping

# Create your views here.
def index(request):
    items = MenuItem.objects.all()
    current_user = request.user
    context = {
        "user": current_user,
        "reg_pizzas": items.filter(name='Regular Pizza').all(),
        "sicilian_pizzas": items.filter(name='Sicilian Pizza').all(),
        "subs": items.filter(category='Sb').all(),
        "pastas": items.filter(category='Ps').all(),
        "salads": items.filter(category='Sd').all(),
        "platters": items.filter(category='Dn').all(),
        "toppings": Topping.objects.order_by('name')
    }
    return render(request, 'orders/index.html', context)

def detail(request, item_id):
    item = get_object_or_404(MenuItem, pk=item_id)
    context = {
        "item": item,
        "item_toppings": item.toppings.all(),
        "other_toppings": Topping.objects.exclude(name=item).all()
    }
    return render(request, "orders/detail.html", context)
