from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from products.models import Product

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_items')
    quantity = models.PositiveIntegerField(default=1)
    size = models.CharField(max_length=20, default="") 

    def total_price(self):
        return self.product.price * self.quantity

class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    session_id = models.CharField(max_length=128, null=True, blank=True)  # Store session ID for anonymous users
    items = models.ManyToManyField(CartItem, blank=True)

    def total_price(self):
        return self.items.aggregate(Sum('product__price'))['product__price__sum'] or 0

    def __str__(self):
        if self.user:
            return f"Cart for {self.user.username}"
        else:
            return "Anonymous Cart"
