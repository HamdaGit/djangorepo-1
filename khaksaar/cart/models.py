from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from products.models import Product 
# Create your models here.

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.product.price * self.quantity

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem, blank=True)
    
    def total_price(self):
        return self.items.aggregate(Sum('product__price'))['product__price__sum'] or 0

    def __str__(self):
        return f"Cart for {self.user.username}"
