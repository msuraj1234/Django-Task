"""test7 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from test7Aapp import views as a
from test7Bapp import views as b

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1view1', a.mul1view1, name='mul1'),
    path('app1view2', a.mul1view2, name='mul1'),
    path('app2view1', b.mul1view1, name='mul2'),
    path('app2view2', b.mul1view2, name='mul2')
]
