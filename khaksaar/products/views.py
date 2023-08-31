from django.shortcuts import render, get_object_or_404  # Import your sample product data from the products module
from .models import Product

def product_list(request):
    product = Product.objects.all()
    context = {
        'products': product,  # Use your sample product data from the products module
    }
    return render(request, 'products.html', context)

def productdetails(request, productIndex):
    product = Product.objects.all()
    product = get_object_or_404(Product, pk=productIndex)
    context = {
        'product': product,
        'productIndex': productIndex,
    }
    return render(request, 'productdetails.html', context)
        
