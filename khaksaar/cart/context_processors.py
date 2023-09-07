# Create a new Python file in your app (e.g., cart/context_processors.py)

from .models import Cart

def cart_count(request):
    # Fetch the user's cart and count the items
    cart = None
    if request.user.is_authenticated:
        cart, _ = Cart.objects.get_or_create(user=request.user)
    elif request.session.get('cart_id'):
        cart, _ = Cart.objects.get_or_create(session_id=request.session['cart_id'])

    cart_item_count = cart.items.count() if cart else 0

    return {'cart_item_count': cart_item_count}
