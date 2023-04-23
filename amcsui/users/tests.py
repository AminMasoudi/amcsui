from django.test import TestCase, Client

from .models import UserProfile, User
from .forms import LoginForm
# Create your tests here.

class UsersTestCase(TestCase):
    def setUp(self) -> None:
        a = User.objects.create_user(username="test",password="whatch0ut")
        UserProfile.objects.create(user=a)


    def test_index(self):
        c = Client()
        response = c.get("/users/")
        self.assertEqual(response.status_code,302)


    def test_login(self):
        c = Client()
        response = c.post("/users/login_view",{"username":"test",
                                               "password": "whatch0ut"})
        self.assertEqual(response.status_code, 302)

    def test_sign_up(self):
        c = Client()
        passwords = "whatch0ut"
        response = c.post("/users/signup",{"username":"test2",
                                           "email":"a@gg.co",
                                           "password1":passwords,
                                           "password2":passwords})
        self.assertEqual(response.status_code,302,response.cookies)
        self.assertEqual(response.url,"/users/")