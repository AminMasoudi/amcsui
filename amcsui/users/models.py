
from django.contrib.auth.models import User
from flights.models import Flight 
from django.db import models


class UserProfile(models.Model):
    user     = models.OneToOneField(User,primary_key=True, on_delete=models.CASCADE)
    email    = models.EmailField()
    # TODO :add through= to many to many
    trips    = models.ManyToManyField(Flight, blank=True, related_name="passengers")
    credit   = models.IntegerField(default=1000)
    

    def __str__(self) -> str:
        return f"<{self.pk}: {self.user.username}>"
    
    def is_valid(self):
        return (self.credit >=0)
    
    def buy(self,product_price):
        if product_price<self.credit:
            self.credit -= product_price
            return True
        else:
            return False
        #TODO: take product and add it to user_profile