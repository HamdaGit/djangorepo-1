from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseNotAllowed
from products.models import Product
from .models import Cart, CartItem

def add_to_cart(request, productIndex):
    if request.method == 'POST':
        size = request.POST.get('size')
        product = get_object_or_404(Product, pk=productIndex)

        # Check if there's an existing cart for the user or create a new one
        if request.user.is_authenticated:
            cart, created = Cart.objects.get_or_create(user=request.user)
        else:
            # For anonymous users, use session_id to create a cart
            session_id = request.session.get('cart_id')
            if session_id:
                cart, created = Cart.objects.get_or_create(session_id=session_id)
            else:
                cart = Cart.objects.create(session_id=request.session.session_key)

        # Create or update cart item
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product, size=size)
        if not created:
            cart_item.quantity += 1
            cart_item.save()

        # Update the session cart_id for anonymous users
        if not request.user.is_authenticated:
            request.session['cart_id'] = cart.session_id
        
        print("Cart:", cart)
        print("Cart Items:", cart.items.all())

        return render(request, 'cart.html', {'cart': cart, 'cart_items': cart_item})

    else:
        return HttpResponseNotAllowed(['POST'])
