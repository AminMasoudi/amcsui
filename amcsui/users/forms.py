from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login


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

class Signup(forms.Form):
    username = forms.CharField(max_length=65, required=True)
    password = forms.CharField(max_length=65, required=True,widget=forms.PasswordInput)

class Registeration_form(UserCreationForm):
    username = forms.CharField(max_length=65)
    email = forms.EmailField()
