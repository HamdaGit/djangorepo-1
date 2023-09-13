from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseNotAllowed
from products.models import Product
from .models import Cart, CartItem,Order
from django.contrib.sessions.models import Session
from django.http import HttpResponseForbidden

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
    
        return render(request, 'cart.html', {'cart': cart, 'cart_items': cart_items, 'productindex':productIndex})
    else:
        return HttpResponseNotAllowed(['POST'])


def remove_from_cart(request, productIndex):
    if request.method == 'POST':
        cart_item = get_object_or_404(CartItem, pk=productIndex)
        if cart_item.cart and hasattr(cart_item.cart, 'session_id'):
            session_id = request.session.session_key
            if cart_item.cart.session_id == session_id:
                cart_item.delete()
        return redirect('cart:cart')  # Redirect back to the cart page
    
    # GET request handling removed for now
    
    return HttpResponseForbidden()
def checkout(request):
    if request.method == 'POST':
         # Get the cart associated with the current session
        cart = Cart.objects.get_cart(request)
        cart_items = cart.get_cart_items()

        # Calculate the total price
        total_price = sum(item.total_price() for item in cart_items)

        # Create an instance of the Order model with the collected data
        order = Order(
            user=request.user if request.user.is_authenticated else None,
            billing_name=request.POST.get('billing_name'),
            billing_address=request.POST.get('billing_address'),
            billing_phone = request.POST.get('billing_phone'),
            shipping_name=request.POST.get('shipping_name'),
            shipping_address=request.POST.get('shipping_address'),
            shipping_phone = request.POST.get('shipping_phone'),
            # Add more fields as needed
            total_price=total_price  # You'll need to calculate the total price
        )

        # Save the order to the database
        order.save()

        # Redirect to a thank-you page or some other confirmation page
        return render(request, 'order.html',{'order': order})  # Adjust the URL pattern name as needed

    else:
        # Handle the GET request to display the checkout form
        cart = Cart.objects.get_cart(request)
        cart_items = cart.get_cart_items()
        return render(request, 'checkout.html', {'cart': cart, 'cart_items': cart_items})


def cart(request):
    cart = Cart.objects.get_cart(request)
    cart_items = cart.get_cart_items()
    return render(request, 'cart.html', {'cart': cart, 'cart_items': cart_items})

def order(request):
    
    return render(request, 'order.html')

