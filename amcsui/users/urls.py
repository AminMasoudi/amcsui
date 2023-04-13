from django.urls import path
from . import views
app_name = 'users'

urlpatterns = [
    path("", views.index, name="index"),
    path("login_view", views.login_view, name="login_view"),
    path("signup", views.signup, name="sign_up"),
]