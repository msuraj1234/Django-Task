from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home, name = 'home' ),
    path('service', views.service, name = 'service' ),
    path('contact', views.contact, name = 'contact' ),
    path('about', views.about, name = 'contact' )
]