from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import LoginForm
from .forms import RegistrationForm
from .models import UserProfile

def profile_finder(request):
    ''' finds `UserProfile` if user has been authenticated
     else returns `False`'''
    if request.user.is_authenticated:

        user    = User.objects.get(username=request.user.username)
        profile = UserProfile.objects.get(user=user)
        return profile

    return False


def index_view(request):
    """render `users/index.html` if user is authenticated
    else redirect to `users:login_view`"""

    profile = profile_finder(request)
    if profile:
        return render(request, "users/index.html", {
            "flights": profile.trips.all()
        })
    return HttpResponseRedirect(reverse("users:login_view"))


def log_user_in(request):
    form = LoginForm(request.POST)
    user = form.auth(request)

    if user:
        login(request,user)
        return HttpResponseRedirect(reverse("users:index"))

    messages.error(request,f'Invalid username or password')
    return render(request,'users/login.html',{'form': form})


def sign_up_user(request):
    form = RegistrationForm(request.POST)
    if user:=form.auth():
        login(request, user)
        return HttpResponseRedirect(reverse("users:index"))
    else:
        messages.error(request,"username existed")
        return render(request, "users/sign_up.html", {"form":form})
    