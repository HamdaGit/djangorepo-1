# cart/urls.py
from django.urls import path
from . import views 


app_name = "cart"
urlpatterns = [
   
    path('add_to_cart/<int:productIndex>/', views.add_to_cart, name='add_to_cart'),

    
    # Other URLs
]
