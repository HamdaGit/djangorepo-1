from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseNotAllowed
from products.models import Product
from .models import Cart, CartItem
from django.contrib.sessions.models import Session

# cart/views.py

def add_to_cart(request, productIndex):
    if request.method == 'POST':
        size = request.POST.get('size')
        product = get_object_or_404(Product, pk=productIndex)

        # Check if there's an existing session
        session_id = request.session.session_key
        if not session_id:
            request.session.create()
            session_id = request.session.session_key

        print("Session ID:", session_id)
        
        # Retrieve or create the cart associated with the session
        cart, created = Cart.objects.get_or_create(session_id=session_id)

         # Create or update cart item
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product, size=size)
        if not created:
            cart_item.quantity += 1
            cart_item.save()


        cart_items = cart.get_cart_items()
        
        print("Cart Item:", cart_item)
        print("Cart:", cart)
        print("Form Data:", request.POST)
        print("Cart Items:", cart_items)
        print("Product:", product)
        print("Size:", size)

    
        return render(request, 'cart.html', {'cart': cart, 'cart_items': cart_items})
    else:
        return HttpResponseNotAllowed(['POST'])
