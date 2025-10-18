from django.shortcuts import render, get_object_or_404, redirect
from vulnerable_app.models import Product, Category, Brand, Comment
from django.db.models import Count
from django.core.paginator import Paginator
from django.utils.safestring import mark_safe

def product_index_unsafe(request):
    search_query = request.GET.get('q', '')
    category_id = request.GET.get('category', '')
    min_price = request.GET.get('min_price', 0)
    max_price = request.GET.get('max_price', 5000)
    
    products = Product.objects.all()
    
    if search_query:
        products = products.filter(name__icontains=search_query)
    
    if category_id:
        products = products.filter(category_id=category_id)
    
    products = products.filter(price__gte=min_price, price__lte=max_price)
    
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    products_page = paginator.get_page(page_number)
    
    categories = Category.objects.all().annotate(count=Count('product'))
    brands = Brand.objects.all()
    
    context = {
        'products': products_page,
        'categories': categories,
        'brands': brands,
        'search_query': mark_safe(search_query),
        'total_products': products.count(),
        'unsafe': True
    }
    return render(request, 'product/index.html', context=context)

def product_index_safe(request):
    search_query = request.GET.get('q', '')
    category_id = request.GET.get('category', '')
    min_price = request.GET.get('min_price', 0)
    max_price = request.GET.get('max_price', 5000)
    
    products = Product.objects.all()
    
    if search_query:
        products = products.filter(name__icontains=search_query)
    
    if category_id:
        products = products.filter(category_id=category_id)
    
    products = products.filter(price__gte=min_price, price__lte=max_price)
    
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    products_page = paginator.get_page(page_number)
    
    categories = Category.objects.all().annotate(count=Count('product'))
    brands = Brand.objects.all()
    
    context = {
        'products': products_page,
        'categories': categories,
        'brands': brands,
        'search_query': search_query,
        'total_products': products.count(),
    }
    return render(request, 'product/index.html', context=context)

def product_detail_safe(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    comments = Comment.objects.filter(product=product).order_by('-created_at')
    
    context = {
        'product': product,
        'comments': comments,
    }
    return render(request, 'product/detail.html', context=context)


def product_detail_unsafe(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    comments = Comment.objects.filter(product=product).order_by('-created_at')
        
    context = {
        'product': product,
        'comments': comments,
        'unsafe': True
    }
    return render(request, 'product/detail.html', context=context)


