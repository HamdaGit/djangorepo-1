from django.urls import path
from . import views

app_name = "Product1"

urlpatterns = [
    path("detail/", views.product_list, name="product_list"),
    path("detail/<int:productIndex>/", views.productdetails, name="productdetails"),
]
