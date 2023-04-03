from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Category,Products
from django.core.paginator import Paginator,EmptyPage,InvalidPage

# Create your views here.
# def index(request):
#     return HttpResponse("hey am here")
def allProdCat (request,c_slug=None):

    c_Page=None
    Product_list=None
    if c_slug != None:

        c_Page=get_object_or_404 (Category,slug=c_slug)

        Product_list=Products.objects.all().filter(category=c_Page,available=True)

    else:

        Product_list=Products.objects.all().filter(available=True)
    paginator=Paginator(   Product_list,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        product=paginator.page(page)
    except:
        product=paginator.page(paginator.num_pages)

    return render (request,"category.html",{'category':c_Page,'products':product})

def  proDetail (request,c_slug,product_slug):

    try:
        product=Products.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e

    return render (request,'product.html',{'product':product})