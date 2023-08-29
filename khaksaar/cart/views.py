from django.shortcuts import redirect, render
from django.http import HttpResponseNotAllowed
from products.models import Product
from .models import Cart, CartItem

def add_to_cart(request, product_id):
    if request.method == 'POST':
        user = request.user
        size = request.POST.get('size')
        product = Product.objects.get(pk=product_id)
        cart, created = Cart.objects.get_or_create(user=user)
        
        # Create or update cart item
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product, size=size)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        
        return redirect('cart:cart')  # Redirect to the cart page
    
    else:
        return HttpResponseNotAllowed(['POST'])
