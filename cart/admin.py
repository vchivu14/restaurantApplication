from django.contrib import admin
from .models import OrderItem, Order
# Register your models here.

class OrderItemsInLine(admin.TabularInline):
    model = Order.items.through
    verbose_name_plural = "Items"

class OrderAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Order', {'fields': ('ref_code',)}),
        ('Customer', {'fields':('customer',)}),
    ]
    inlines = [
        OrderItemsInLine,
    ]
    list_display = ('ref_code', 'date_ordered')
    list_filter = ('customer',)
    exclude = ('items',)
    
class OrderItemAdmin(admin.ModelAdmin):
    list_filter = ('date_ordered',)


admin.site.register(OrderItem,OrderItemAdmin)
admin.site.register(Order,OrderAdmin)