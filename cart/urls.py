from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    path('add-to-cart/<int:item_id>/', views.add_to_cart, name="add_to_cart"),
    path('item-to-delete/<int:item_id>', views.delete_from_cart, name="delete_item"),
    path('order-summary/', views.order_details, name="order_details"),
    path('checkout/<int:order_id>', views.checkout, name="checkout")
]