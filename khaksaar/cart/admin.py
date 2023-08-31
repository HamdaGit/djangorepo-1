from django.contrib import admin
from products.models import Product 
from .models import CartItem, Cart

# Register your models here.

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'size')
    # Add more fields if needed

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_price')
    filter_horizontal = ('items',)