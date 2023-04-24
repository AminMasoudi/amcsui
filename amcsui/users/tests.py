from django.test import TestCase, Client

from .models import UserProfile, User
from .forms import LoginForm
# Create your tests here.

class UsersTestCase(TestCase):
    def setUp(self) -> None:
        self.username = "test"
        self.password = "whatch0ut"
        a = User.objects.create_user(username=self.username, password=self.password)
        UserProfile.objects.create(user=a)

    def test_index(self):
        c = Client()
        response = c.get("/users/")
        self.assertEqual(response.status_code,302)


    def test_login_view(self):
        c = Client()
        response = c.post("/users/login_view",{"username":self.username,
                                               "password": self.password})

        self.assertEqual(response.status_code, 302)

    def test_login_logout(self):
        c = Client()
        c.login(username=self.username, password=self.password)
        response = c.get("/users/")
        self.assertEqual(response.status_code,200)
        c.logout()
        response = c.get("/users/")
        self.assertEqual(response.status_code,302)



    def test_sign_up_view(self):
        c = Client()
        self.password = "whatch0ut"
        response = c.post("/users/signup",{"username":"test2",
                                           "email":"a@gg.co",
                                           "password1":self.password,
                                           "password2":self.password})     
        self.assertEqual(response.status_code,302,response.cookies)
        self.assertEqual(response.url,"/users/")

    def test_logout(self):
        c = Client()
        c.login(username=self.username, password=self.password)
        
        c.logout()

#TODO: test logout

#TODO: test froude logins and ...