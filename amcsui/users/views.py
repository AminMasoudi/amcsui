from django.contrib.auth import login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import LoginForm
from .forms import Registeration_form
from .helper_functions import LogUserIn, user_index, sign_up_user
# Create your views here.


#index view
#shows the trips of user if authenticated else redirect to login
def index(request):

    return user_index(request)



#Login Page
def login_view(request):
    if request.method == "POST":
        LogUserIn(request)
    
    return render(request, "users/login.html", {"form": LoginForm()})



#Signup Page
def signup(request):
    if request.method == "POST":
        return sign_up_user(request)

    if request.user.is_authenticated:
        logout(request)
    return render(request, "users/sign_up.html", {"form": Registeration_form()})
                
