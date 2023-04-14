from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import LoginForm, Registeration_form
from .models import User, UserProfile
# Create your views here.


#index view
#shows the trips of user if authenticated else redirect to login
from .helper_functions import user_index
def index(request):

    return user_index(request)


from .helper_functions import LogUserIn
def login_view(request):
    if request.method == "POST":
        LogUserIn(request)
    
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
                passenger = UserProfile.objects.create(user=user, email=email)
                passenger.save()
                login(request, user)
                return HttpResponseRedirect(reverse("users:user/index"))
            else:
                messages.error(request,"username existed")
        return render(request, "users/sign_up.html", {"form":form})
    if request.user.is_authenticated:
        logout(request)
    return render(request, "users/sign_up.html", {"form": Registeration_form()})
                

    