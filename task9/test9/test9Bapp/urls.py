from django.contrib import admin
from django.urls import path
from test9Bapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('url11', views.url9A1, name='mul1'),
    path('url12', views.url9B2, name='mul2'),
]