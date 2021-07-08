from django.contrib import admin
from django.urls import path
from test9Aapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('url1', views.url9A, name='mul1'),
    path('url2', views.url9B, name='mul2'),
]