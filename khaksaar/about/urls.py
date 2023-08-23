from django.urls import path
from .import  views 

app_name="About"
urlpatterns = [ 
    path("about/", views.about,name="about")
]
