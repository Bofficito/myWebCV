from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls, name = 'admin'),
    path('', views.home, name='base'),
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery, name='gallery'),  
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)