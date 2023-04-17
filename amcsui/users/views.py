from django.contrib.auth import login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import LoginForm
from .forms import RegistrationForm
from .helpers import log_user_in, index_view, sign_up_user
# Create your views here.


#index view
#shows the trips of user if authenticated else redirect to login
def index(request):

    return index_view(request)



#Login Page
def login_view(request):
    if request.method == "POST":
        return log_user_in(request)
    
    return render(request, "users/login.html", {"form": LoginForm()})



#Signup Page
def sign_up(request):
    if request.method == "POST":
        return sign_up_user(request)

    if request.user.is_authenticated:
        logout(request)
    return render(request, "users/sign_up.html", {"form": RegistrationForm()})
                
#Log out url
def logout_(request):
    logout(request)
    return HttpResponseRedirect(reverse("users:login_view"))