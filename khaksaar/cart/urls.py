# cart/urls.py
from django.urls import path
from . import views 


app_name = 'cart'
urlpatterns = [
   
    path('add_to_cart/<int:productIndex>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:productIndex>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.cart, name='cart'),
    path("checkout/", views.checkout, name="checkout"),  
    path('order/', views.order, name='order'),   
]
    
    # Other URLs

