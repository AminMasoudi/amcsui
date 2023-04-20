from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.models import User
from users.models import UserProfile

from .helpers import book_view
from .models import *
# from .forms import BookingForm
# Create your views here.



def index(request):
    flights = Flight.objects.all()
    return render(request, "flights/index.html", {
        "flights": flights
    })

def book(request):
    return book_view(request)