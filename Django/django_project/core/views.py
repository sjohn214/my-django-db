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
from django.shortcuts import render
from .models import Customer

# Customer Search Feature
from .models import customers, orders

def customer_search(request):
    query = request.GET.get('q', '').strip()
    
    if query:
        # Look up records matching criteria and optimize matching orders
        customer_list = customers.objects.filter(
            Q(company_name__icontains=query) |
            Q(contact_name__icontains=query) |
            Q(city__icontains=query)
        ).prefetch_related('orders_set') # Django automatically assigns lowercase set managers
    else:
        customer_list = customers.objects.all().prefetch_related('orders_set')
        
    paginator = Paginator(customer_list, 10)
    page_number = request.GET.get('page')
    
    try:
        results = paginator.page(page_number)
    except PageNotAnInteger:
        results = paginator.page(1)
    except EmptyPage:
        results = paginator.page(paginator.num_pages)
        
    return render(request, 'customer_search.html', {'results': results, 'query': query})


# Product Search Feature
from .models import products, Categories  # Ensure uppercase Categories is imported

def product_search(request):
    query = request.GET.get('q', '').strip()
    category_id = request.GET.get('category', '').strip()
    
    # Base Queryset
    product_list = products.objects.all()
    
    # Apply text filter
    if query:
        product_list = product_list.filter(product_name__icontains=query)
        
    # Apply category dropdown filter
    if category_id:
        product_list = product_list.filter(category_id=category_id)
        
    # Fetch all categories to populate the dropdown filter options
    all_categories = Categories.objects.all().order_by('category_name')
        
    # Implement pagination (15 items per page)
    paginator = Paginator(product_list, 15)
    page_number = request.GET.get('page')
    
    try:
        results = paginator.page(page_number)
    except PageNotAnInteger:
        results = paginator.page(1)
    except EmptyPage:
        results = paginator.page(paginator.num_pages)
        
    context = {
        'results': results, 
        'query': query,
        'selected_category': category_id,
        'categories': all_categories
    }
    return render(request, 'product_search.html', context)


# Backend view controller
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import customers, products

def customer_search(request):
    query = request.GET.get('q', '').strip()
    
    if query:
        # Searches across Company Name, Contact Name, and City fields
        results = customers.objects.filter(
            Q(company_name__icontains=query) |
            Q(contact_name__icontains=query) |
            Q(city__icontains=query)
        )
    else:
        results = customers.objects.all()[:50] # Caps initial load for optimization
        
    return render(request, 'customer_search.html', {'results': results, 'query': query})

def product_search(request):
    query = request.GET.get('q', '').strip()
    
    if query:
        # Query matches against item name
        results = products.objects.filter(product_name__icontains=query)
    else:
        results = products.objects.all()[:50]
        
    return render(request, 'product_search.html', {'results': results, 'query': query})

def product_detail(request, product_id):
    # Fetch specific object using primary key 'product_id'
    product = get_object_or_404(products, product_id=product_id)
    return render(request, 'product_detail.html', {'product': product})

# To reduce performance bottlenecks import Paginator

from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import customers, products

def customer_search(request):
    query = request.GET.get('q', '').strip()
    
    if query:
        customer_list = customers.objects.filter(
            Q(company_name__icontains=query) |
            Q(contact_name__icontains=query) |
            Q(city__icontains=query)
        )
    else:
        customer_list = customers.objects.all()
        
    # Group into blocks of 10 items per page
    paginator = Paginator(customer_list, 10)
    page_number = request.GET.get('page')
    
    try:
        results = paginator.page(page_number)
    except PageNotAnInteger:
        results = paginator.page(1)  # Fallback to page 1 if page isn't an integer
    except EmptyPage:
        results = paginator.page(paginator.num_pages)  # Deliver last page if out of bounds
        
    return render(request, 'customer_search.html', {'results': results, 'query': query})

def product_search(request):
    query = request.GET.get('q', '').strip()
    
    if query:
        product_list = products.objects.filter(product_name__icontains=query)
    else:
        product_list = products.objects.all()
        
    # Group into blocks of 15 items per page
    paginator = Paginator(product_list, 15)
    page_number = request.GET.get('page')
    
    try:
        results = paginator.page(page_number)
    except PageNotAnInteger:
        results = paginator.page(1)
    except EmptyPage:
        results = paginator.page(paginator.num_pages)
        
    return render(request, 'product_search.html', {'results': results, 'query': query})
