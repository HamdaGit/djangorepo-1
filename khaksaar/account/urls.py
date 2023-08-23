from django.urls import path
from .import  views 

app_name="Account"
urlpatterns = [ 
    path("account/", views.account,name="account")
]
