from django.db import models
from django.contrib.auth.models import User
from wines.models import Wine

class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='wishlist')
    wines = models.ManyToManyField(Wine, related_name='wishlisted_by')

    def __str__(self):
        return f"{self.user.username}'s Wishlist"