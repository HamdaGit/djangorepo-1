from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from products.models import Product

def index(request, productIndex=None):  # Provide a default value of None
    if productIndex is not None:
        product = get_object_or_404(Product, pk=productIndex)
    else:
        product = None  # Handle the case where productIndex is None
    context = {
        'product': product,
        'productIndex': productIndex,
    }
    return render(request, 'index.html', context)
