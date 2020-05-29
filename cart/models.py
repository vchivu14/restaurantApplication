from django.db import models
from django.contrib.auth import get_user_model
from orders.models import MenuItem
from users.models import Profile
# Create your models here.

User = get_user_model()

class OrderItem(models.Model):
    item = models.OneToOneField(MenuItem, on_delete=models.SET_NULL, null=True)
    date_ordered = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.item.name

class Order(models.Model):
    ref_code = models.CharField(max_length=15)
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    items = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(auto_now=True)
    
    def get_cart_items(self):
        return self.items.all()
    
    def get_cart_total(self):
        return sum([item.item.price for item in self.items.all()])
    
    def __str__(self):
        return '{0} - {1}'.format(self.customer, self.ref_code)
