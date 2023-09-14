from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from products.models import Product



class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_items')
    quantity = models.PositiveIntegerField(default=1)
    size = models.CharField(max_length=20, default="") 
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, related_name='cart_items', default=None, null=True, blank=True)

    def total_price(self):
        return self.product.price * self.quantity
    
class CartManager(models.Manager):
    def get_cart(self, request):
        session_id = request.session.session_key
        if not session_id:
            request.session.create()
            session_id = request.session.session_key 

        cart, created = self.get_or_create(session_id=session_id)
        return cart

class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    session_id = models.CharField(max_length=128, null=True, blank=True)  # Store session ID for anonymous users
    objects = CartManager()
   
    def get_cart_items(self):
        return CartItem.objects.filter(cart=self)

    def total_price(self):
        cart_items = self.get_cart_items()
        return sum(item.total_price() for item in cart_items)

    def __str__(self):
        if self.user:
            return f"Cart for {self.user.username}"
        else:
            return "Anonymous Cart"
        


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)   
    billing_name = models.CharField(max_length=100)
    billing_address = models.TextField()
    billing_phone = models.CharField(max_length=15, null=True, blank=True)
    shipping_name = models.CharField(max_length=100)
    shipping_address = models.TextField()
    shipping_phone = models.CharField(max_length=15, null=True, blank=True)
    
    # Add more fields as needed
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Order #{self.id}"
