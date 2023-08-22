

from django.urls import path
from .import  views 

app_name="Product1"
urlpatterns = [ 
    path("detail/", views.product,name="detail")
]


