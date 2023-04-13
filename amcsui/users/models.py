
from django.contrib.auth.models import User
from django.db import models
from flights.models import Flight 
class userProfile(models.Model):
    user     = models.OneToOneField(User,primary_key=True, on_delete=models.CASCADE)
    email    = models.EmailField()
    trips    = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__(self) -> str:
        return f"<{self.pk}: {self.user.username}>"
    
