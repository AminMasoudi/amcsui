from django.test import TestCase, Client

from .models import UserProfile, User
# Create your tests here.

class UsersTestCase(TestCase):

    def test_index(self):
        c = Client()
        response = c.get("/users/")
        self.assertEqual(response.status_code,302)