from django.shortcuts import render
from .models import Product
# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, "products/index.html",{"products":products})

def products_view(request,name):
    product = Product.objects.get(name=name)
    return render(request, "products/_view.html", {"product":product})

def add_to_cart(request):
    raise NotImplementedError
    