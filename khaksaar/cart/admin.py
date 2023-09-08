
from django.contrib import admin
from products.models import Product
from .models import CartItem, Cart

# Register your models here.

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'size')
    # Add more fields if needed

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'session_id', 'total_price')  # Display both user and session_id
 

    def user(self, obj):
        if obj.user:
            return obj.user.username
        return "Anonymous User"
    user.short_description = 'User'  # Display a more descriptive column name for user