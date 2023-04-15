from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from .models import UserProfile

class LoginForm(forms.Form):
    username = forms.CharField(max_length=65, required=True)
    password = forms.CharField(max_length=65, required=True,widget=forms.PasswordInput)

    def auth(self,request):
        if self.is_valid:
            username = self.cleaned_data["uesrname"]
            password = self.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            return user
        return False




class Registeration_form(UserCreationForm):
    username = forms.CharField(max_length=65)
    email = forms.EmailField()

    def is_unique_username(self):
        if self.is_valid():    
            user = User.objects.filter(username=self.cleaned_data["username"])
            if user:
                return False
            return True
        return False


    def auth(self):
        if self.is_unique_username():
            user = User.objects.create_user(username=self.cleaned_data["username"],
                                            email=self.cleaned_data["email"],
                                            password=self.clean_password2())
            profile = UserProfile.objects.create(user=user,
                                                 email=user.email)
            profile.save()
            return user

        return False