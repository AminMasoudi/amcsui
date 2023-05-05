from django.test import TestCase, Client
from django.urls import reverse
from .models import UserProfile, User
from .forms import LoginForm
from helpers import profile_finder
# Create your tests here.


class UsersTestCase(TestCase):

    def setUp(self) -> None:
        self.username = "test"
        self.password = "whatch0ut"
        a = User.objects.create_user(username=self.username, password=self.password)
        UserProfile.objects.create(user=a)
        
        b = User.objects.create_user(username="rand", password="qwerty")
        UserProfile.objects.create(user=b,credit=-100)

    def test_index(self):
        c = Client()
        response = c.get(reverse("users:index"))
        self.assertEqual(response.status_code, 302)

    def test_login_logout(self):
        c = Client()
        c.login(username=self.username, password=self.password)
        response = c.get(reverse("users:index"))
        self.assertEqual(response.status_code, 200)
        c.logout()
        response = c.get(reverse("users:index"))
        self.assertEqual(response.status_code, 302)

    def test_login_view(self):
        c = Client()
        get_response = c.get(reverse("users:login_view"))
        post_response = c.post(reverse("users:login_view"), {"username": self.username,
                                                             "password": self.password})

        self.assertEqual(post_response.status_code, 302)
        self.assertEqual(get_response.status_code, 200)

    def test_sign_up_view(self):
        c = Client()
        response = c.post(reverse("users:sign_up"), {"username": "test2",
                                                     "email": "a@gg.co",
                                                     "password1": self.password,
                                                     "password2": self.password})     
        self.assertEqual(response.status_code, 302, response.cookies)
        self.assertEqual(response.url, reverse("users:index"))

    def test_logout(self):
        c = Client()
        c.login(username=self.username, password=self.password)
        response = c.get(reverse("users:logout"))
        self.assertEqual(response.status_code, 302, response.cookies)
    def test_validation(self):
        user = UserProfile.objects.get(credit=-100)
        self.assertEqual(user.is_valid(),False)
        user = User.objects.get(username=self.username)
        user = UserProfile.objects.get(user=user)
        self.assertEqual(user.is_valid(),True)
# TODO: test froude logins and ...
    def test_user_buy(self):
        user = User.objects.get(username=self.username)
        user = UserProfile.objects.get(user=user)
        self.assertEqual(user.buy(20),True)
        self.assertEqual(user.buy(10000),False)
