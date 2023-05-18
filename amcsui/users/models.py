
from django.contrib.auth.models import User
from flights.models import Flight 
from django.db import models
from products.models import Product

class UserProfile(models.Model):
    user     = models.OneToOneField(User,primary_key=True, on_delete=models.CASCADE)
    email    = models.EmailField()
    # TODO :add through= to many to many
    trips    = models.ManyToManyField(Flight, blank=True, related_name="passengers")
    credit   = models.IntegerField(default=1000)
    cart     = models.ManyToManyField(Product, blank=True)
    
    

    def __str__(self) -> str:
        return f"<{self.pk}: {self.user.username}>"
    
    def is_valid(self):
        return (self.credit >=0)
    
    def buy(self,product:Product):
        if product.price < self.credit:
            self.credit -= product.price
            self.cart.add(product)
            return True
        else:
            return False