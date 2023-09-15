from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from cart.models import CartItem, Cart

def index(request):  # Provide a default value of None
    # In your view
        cart = Cart.objects.get_cart(request)

        cart_items = CartItem.objects.filter(cart=cart)  # Replace some_cart with your actual cart
        context = {
            'cart_items': cart_items,
}
        return render(request, 'index.html', context)

  
