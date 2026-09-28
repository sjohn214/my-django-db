"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from core.views import home_view, customer_list_view  # <-- Update this import line


urlpatterns = [
    path('admin/', admin.site.urls),
]

# Build product detail feature
from django.urls import path
from . import views

urlpatterns = [
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
]

# Class-based views
from django.urls import path
from . import views

urlpatterns = [
    path('customers/', views.customer_search, name='customer_search'),
    path('products/', views.product_search, name='product_search'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
]
