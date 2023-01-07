from django.shortcuts import render
from .models import *

# Home page
def home(request):
    banners=Banner.objects.all().order_by('-id')
    data=Product.objects.filter(is_featured=True).order_by('-id')
    return render(request, 'index.html', {'data':data, 'banners':banners})

# Category
def category_list(request):
    data=Category.objects.all().order_by('-id')
    return render(request, 'category_list.html', {'data':data})

#Brand
def brand_list(request):
    data=Brand.objects.all().order_by('-id')
    return render(request, 'brand_list.html', {'data':data})

#product list
def product_list(request):
    data=Product.objects.all().order_by('-id')
    cats=Product.objects.distinct().values('category__title','category__id')
    brands=Product.objects.distinct().values('brand__title','brand__id')
    colors=Product.objects.distinct().values('color__title','color__id','color__color_code')
    sizes=Product.objects.distinct().values('size__title','size__id')
    return render(request, 'product_list.html', 
    {
        'data':data,
        'cats':cats,
        'brands':brands,
        'colors': colors,
        'sizes': sizes,
    }
    )

#product list according to category
def category_product_list(request,cat_id):
    category=Category.objects.get(id=cat_id)
    data=Product.objects.filter(category=category).order_by('-id')
    cats=Product.objects.distinct().values('category__title','category__id')
    brands=Product.objects.distinct().values('brand__title','brand__id')
    colors=Product.objects.distinct().values('color__title','color__id','color__color_code')
    sizes=Product.objects.distinct().values('size__title','size__id')
    return render(request, 'category_product_list.html',
    {
        'data':data,
        'cats':cats,
        'brands':brands,
        'colors': colors,
        'sizes': sizes,
    })

#product list according to brand
def brand_product_list(request,brand_id):
    brand=Brand.objects.get(id=brand_id)
    data=Product.objects.filter(brand=brand).order_by('-id')
    cats=Product.objects.distinct().values('category__title','category__id')
    brands=Product.objects.distinct().values('brand__title','brand__id')
    colors=Product.objects.distinct().values('color__title','color__id','color__color_code')
    sizes=Product.objects.distinct().values('size__title','size__id')
    
    return render(request, 'category_product_list.html',
    {
        'data':data,
        'cats':cats,
        'brands':brands,
        'colors': colors,
        'sizes': sizes,
        
    })

# Product detail
def product_detail(request,slug,id):
    product=Product.objects.get(id=id)
    related_products=Product.objects.filter(category=product.category).exclude(id=id)[:4]
    return render(request, 'product_detail.html',{'data':product,'related':related_products})

# search
# def search(request):
#     q=request.GET['q']
#     data=Product.objects.filter(title_icontains=q).order_by('-id')
#     return render(request, 'search.html', {'data':data})