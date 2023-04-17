from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Airport(models.Model):
    city = models.CharField(max_length=64)
    code = models.CharField(max_length=3)

    def __str__(self) -> str:
        return f"{self.code}"


class Flight(models.Model):
    origin      = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departure")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrival")
    duration    = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.pk}:from {self.origin} to {self.destination}"

    def is_valid_flight(self):
        return self.destination != self.origin and self.duration > 0