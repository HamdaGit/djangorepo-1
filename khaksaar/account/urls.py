from django.urls import path
from .import  views 

app_name="Account"
urlpatterns = [ 
    path("account/", views.account,name="account"),
    path("signup/", views.signup, name="signup"),  
    path("login/", views.login, name="login"),     
]