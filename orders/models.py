from django.db import models

# Create your models here.
class Topping(models.Model):
    name = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
    
    def __str__(self):
        return f"{self.name}"

class MenuItem(models.Model):
    categories = [
        ('Pz','Pizzas'),
        ('Sb','Subs'),
        ('Ps','Pastas'),
        ('Sd','Salads'),
        ('Dn','Dinner'),
    ]
    category = models.CharField(max_length=2, choices=categories, blank=True)
    name = models.CharField(max_length=80)
    toppings = models.ManyToManyField(Topping, blank=True)
    sizes = (
        ('S', 'Small'),
        ('L', 'Large'),
        ('X', 'Extra Large'),
        )
    item_size = models.CharField(max_length=1, choices=sizes, blank=True)
    toppings_extra = models.PositiveIntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self):
        return f"{self.name} - {self.item_size} - {self.toppings_extra} - {self.price}"