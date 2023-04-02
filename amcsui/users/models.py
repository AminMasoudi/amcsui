from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=64)
    email    = models.EmailField()

    def __str__(self) -> str:
        return f"<{self.id}: {self.username}>"

        