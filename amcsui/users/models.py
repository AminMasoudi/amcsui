
from django.contrib.auth.models import User
from flights.models import Flight 
from django.db import models


class UserProfile(models.Model):
    user     = models.OneToOneField(User,primary_key=True, on_delete=models.CASCADE)
    email    = models.EmailField()
    # add through= to many to many
    trips    = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__(self) -> str:
        return f"<{self.pk}: {self.user.username}>"
    