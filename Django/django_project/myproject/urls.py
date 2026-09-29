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
from core import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 1. Home / Product Catalog
    path('', views.home_view, name='home'),
    
    # 2. Customer List & Search
    path('customers/', views.customer_list_view, name='customer_list'),
    path('customers/search/', views.customer_search, name='customer_search'),
    
    # 3. Product Search & Detail
    path('products/search/', views.product_search, name='product_search'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
]

