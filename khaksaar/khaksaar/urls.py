
from django.contrib import admin
from django.urls import path,include
from .import  views 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns = [ 
    path("admin/", admin.site.urls),
    path("home/", views.index, name="home"),
    path("home/",include('products.urls')),
    path("home/",include('contact.urls')),
    path("home/",include('about.urls')),
    path("home/",include('account.urls')),
]


urlpatterns += staticfiles_urlpatterns()
