from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import LoginForm
from .forms import RegistrationForm
from .models import UserProfile
from helpers import profile_finder
import logging

logger = logging.getLogger(__name__)

def index_view(request):
    """render `users/index.html` if user is authenticated
    else redirect to `users:login_view`"""

    profile = profile_finder(request)
    if profile:
        return render(request, "users/index.html", {
            "flights": profile.trips.all()
        })
    logger.debug("not loged in")
    return HttpResponseRedirect(reverse("users:login_view"))


def log_user_in(request):
    form = LoginForm(request.POST)
    user = form.auth(request)

    if user:
        login(request,user)
        return HttpResponseRedirect(reverse("users:index"))
    logger.debug('Invalid username or password')
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
    