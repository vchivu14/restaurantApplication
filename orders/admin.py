from django.contrib import admin
from .models import Topping, MenuItem
# Register your models here.

class ToppingsItemsInline(admin.TabularInline):
    model = MenuItem.toppings.through
    verbose_name_plural = "Toppings"
    
class MenuItemAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':('category','name')}),
        ('Details', {'fields': ('item_size', 'toppings_extra', 'price')})
    ]
    # inlines = [ToppingInline]
    list_display = ('name', 'category', 'item_size', 'toppings_extra', 'price')
    list_filter = ('category', 'price')
    inlines = [
        ToppingsItemsInline,
    ]
    exclude = ('toppings',)

class ToppingAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['price']
    
admin.site.register(MenuItem, MenuItemAdmin)    
admin.site.register(Topping, ToppingAdmin)