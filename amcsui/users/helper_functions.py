from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import UserProfile
from django.contrib import messages


def ProfileFinder(request):
    ''' finds `UserProfile` if user has been authenticated
     else returns `False`'''
    if request.user.is_authenticated:

        user    = User.objects.get(username=request.user.username)
        profile = UserProfile.objects.get(user=user)
        return profile

    return False



def user_index(request):
    """render `users/index.html` if user is authenticated
    else redirect to `users:login_view`"""

    profile = ProfileFinder(request)
    if profile:
        return render(request, "users/index.html", {
            "flights": profile.trips
        })
    return HttpResponseRedirect(reverse("users:login_view"))


from .forms import LoginForm
def LogUserIn(request):
    form = LoginForm(request.POST)
    user = form.auth(request)

    if user:
        login(request,user)
        return HttpResponseRedirect(reverse("users:index"))

    messages.error(request,f'Invalid username or password')
    return render(request,'users/login.html',{'form': form})
