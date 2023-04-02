from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import (
    authenticate as authenticate,
    logout as logout,
    login as login, 
)


from .models import User
# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    return render(request, "users/index.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,
                            username=username, 
                            password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("users:index"))
        else:
            return render(request, "users/login.html", {"message": "Invalid login"})
    return render(request, "users/login.html")

def Logout(request):
    logout(request)
    return render(request, "users/login.html", {"message" : "you are Loged out"})


# thanks to bing chatbot
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("users:index"))
    else:
        form = UserCreationForm()
    return render(request, 'users/signup.html', {'form': form})