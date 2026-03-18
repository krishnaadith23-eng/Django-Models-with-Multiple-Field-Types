from django.shortcuts import render

# Create your views here.

from .models import Product
def product_list(request): 
    products = Product.objects.all() 
    return render(request, "product_list.html", {"products": products})

def products_price(request):
    products=Product.objects.order_by('price')
    return render(request,"products_price.html",{"products":products})

