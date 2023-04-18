from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.models import User
from users.models import UserProfile
from .models import *
# from .forms import BookingForm
# Create your views here.



def index(request):
    flights = Flight.objects.all()
    return render(request, "flights/index.html", {
        "flights": flights
    })

#TODO: add a helper.py and clean this
#FIXME: dont book twice
def book(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        user_profile = UserProfile.objects.get(user=user)
        if request.method == "POST":
            flights_id = request.POST["flight_id"]
            flights = list(map(lambda x:Flight.objects.get(id=x),flights_id))
            for i in flights:
                user_profile.trips.add(i)
            return HttpResponseRedirect(reverse("users:index"))
        flights = Flight.objects.all()
        return render(request, "flights/book.html", {
            "flights": flights
        })
    return HttpResponseRedirect(reverse("users:login"))