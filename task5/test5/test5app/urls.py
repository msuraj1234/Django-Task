from django.contrib import admin
from django.urls import path
from test5app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index',views.index, name = 'index'),
    path('base',views.base, name = 'index'),
    path('msg',views.msg, name = 'index')
]