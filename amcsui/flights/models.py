from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Airport(models.Model):
    city = models.CharField(max_length=64)
    code = models.CharField(max_length=3)

    def __str__(self) -> str:
        return f"{self.code}"


class Flight(models.Model):
    origin      = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="depature")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="incoming")
    duration    = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.pk}:from {self.origin} to {self.destination}"

