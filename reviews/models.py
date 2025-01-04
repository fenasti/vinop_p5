from django.db import models
from django.contrib.auth.models import User
from wines.models import Wine

class Review(models.Model):

    RATING_CHOICES = (
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    wine = models.ForeignKey(Wine, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField(choices=RATING_CHOICES, default=5)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Review by {self.user.username} on {self.wine.name}'