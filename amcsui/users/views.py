from django.shortcuts import render
from .models import User, userProfile
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, Registeration_form
from django.contrib import messages

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        trips = userProfile.objects.get(user=user).trips.all()
        return render(request,"users/index.html",{
            "user": user,
            "flights": trips
        })
    return HttpResponseRedirect(reverse("users:login_view"))

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse("users:index"))

        messages.error(request,f'Invalid username or password')
        return render(request,'users/login.html',{'form': form})
    
    return render(request, "users/login.html", {"form": LoginForm()})

def signup(request):
    if request.method == "POST":
        form = Registeration_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.clean_password2()
            email    = form.cleaned_data["email"]

            if not User.objects.filter(username=username):
                user = User.objects.create_user(username=username, password=password)
                passenger = userProfile.objects.create(user=user, email=email)
                passenger.save()
                login(request, user)
                return HttpResponseRedirect(reverse("users:user/index"))
            else:
                messages.error(request,"username existed")
        return render(request, "users/sign_up.html", {"form":form})
    if request.user.is_authenticated:
        logout(request)
    return render(request, "users/sign_up.html", {"form": Registeration_form()})
                

    