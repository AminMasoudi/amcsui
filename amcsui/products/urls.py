from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("", views.index, name="index"),
    path("add_to_cart", views.add_to_cart, name="add_to_cart"),
    path("<str:name>", views.products_view, name="_view"),
]