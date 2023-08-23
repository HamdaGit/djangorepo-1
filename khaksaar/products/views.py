from django.shortcuts import render  # Import your sample product data from the products module
from .models import Product
def product_list(request):
    context = {
        'products': Product,  # Use your sample product data from the products module
    }
    return render(request, 'products.html', context)

def productdetails(request, productIndex):
    if productIndex >= 0:
        
        return render(request, 'productdetails.html')
    
