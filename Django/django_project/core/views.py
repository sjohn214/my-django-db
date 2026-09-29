from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import products, customers, orders, Categories

# 1. Product catalog view (Home)
def home_view(request):
    all_products = products.objects.all()[:20] 
    return render(request, 'home.html', {'products': all_products})

# 2. Customer list view
def customer_list_view(request):
    # Note: verify if your model field is 'company_name' or 'companyname'
    try:
        active_customers = customers.objects.all().order_by('company_name')
    except Exception:
        active_customers = customers.objects.all().order_by('companyname')
    return render(request, 'customers.html', {'customers': active_customers})

# 3. Customer Search Feature (with Pagination)
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
        
    paginator = Paginator(customer_list, 10)
    page_number = request.GET.get('page')
    
    try:
        results = paginator.page(page_number)
    except PageNotAnInteger:
        results = paginator.page(1)
    except EmptyPage:
        results = paginator.page(paginator.num_pages)
        
    return render(request, 'customer_search.html', {'results': results, 'query': query})

# 4. Product Search Feature (with Category Dropdown & Pagination)
def product_search(request):
    query = request.GET.get('q', '').strip()
    category_id = request.GET.get('category', '').strip()
    
    product_list = products.objects.all()
    
    if query:
        product_list = product_list.filter(product_name__icontains=query)
        
    if category_id:
        product_list = product_list.filter(category_id=category_id)
        
    # Fetch all categories to populate dropdown filter options
    all_categories = Categories.objects.all().order_by('category_name')
        
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

# 5. Product Detail View
def product_detail(request, product_id):
    product = get_object_or_404(products, product_id=product_id)
    return render(request, 'product_detail.html', {'product': product})
