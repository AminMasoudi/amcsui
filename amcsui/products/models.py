from django.db import models

# Create your models here.

class Product(models.Model):
    name    = models.CharField(max_length=64, blank=False, unique=True)
    price   = models.IntegerField(blank=False)

    def __str__(self) -> str:
        return f"{self.pk}\t:\t{self.name}"