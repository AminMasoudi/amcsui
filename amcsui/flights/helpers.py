from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from helpers import profile_finder
from .models import Flight

def book_view(request):
    user_profile = profile_finder(request)
    if user_profile:
        if request.method == "POST":
            flights_id = request.POST["flight_id"]
            flights = list(map(lambda x: Flight.objects.get(id=x), flights_id))
            for flight in flights:
                #FIXME: add trip if not booked once
                user_profile.trips.add(flight) 
            return HttpResponseRedirect(reverse("users:index"))
        flights = Flight.objects.all()
        return render(request, "flights/book.html", {
            "flights": flights
        })

    return HttpResponseRedirect(reverse("users:login"))