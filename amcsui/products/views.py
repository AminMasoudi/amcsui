from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Product
from helpers import profile_finder
# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, "products/index.html",{"products":products})

def products_view(request,name):
    product = Product.objects.get(name=name)
    return render(request, "products/_view.html", {"product":product})

def add_to_cart(request):
    user = profile_finder(request)
    if user:
        product = Product.objects.get(id=request.POST["product"])
        if user.buy(product):
            return HttpResponseRedirect(reverse("products:index"))
        return HttpResponseRedirect(request.POST.get("path"))
    return HttpResponseRedirect(reverse("users:login_view"))