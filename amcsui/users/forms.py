from django import forms
from django.contrib.auth.forms import UserCreationForm
class LoginForm(forms.Form):
    username = forms.CharField(max_length=65, required=True)
    password = forms.CharField(max_length=65, required=True,widget=forms.PasswordInput)


class Signup(forms.Form):
    username = forms.CharField(max_length=65, required=True)
    password = forms.CharField(max_length=65, required=True,widget=forms.PasswordInput)

class Registeration_form(UserCreationForm):
    username = forms.CharField(max_length=65)
    email = forms.EmailField()
