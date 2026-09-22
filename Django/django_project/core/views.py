from django.shortcuts import render
from .models import products, customers  # <-- Ensure both tables are imported here

# 1. Product catalog view
def home_view(request):
    all_products = products.objects.all()[:20] 
    return render(request, 'home.html', {'products': all_products})

# 2. Customer list view (Make sure 'def' starts at the very edge of the screen!)
def customer_list_view(request):
    active_customers = customers.objects.all().order_by('companyname')
    return render(request, 'customers.html', {'customers': active_customers})



# Create your views here.
