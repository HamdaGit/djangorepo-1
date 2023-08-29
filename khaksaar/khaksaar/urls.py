
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from .import views 

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", views.index, name="home"),
    path("home/", include('products.urls')),
    path("home/", include('contact.urls')),
    path("home/", include('about.urls')),
    path("home/", include('account.urls')),
    path("home/", include('cart.urls')),
]

# Serve media files during development
urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)