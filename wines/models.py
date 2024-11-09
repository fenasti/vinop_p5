from django.db import models


class Wine(models.Model):
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    grapes = models.CharField(max_length=100)  
    country = models.CharField(max_length=100)  
    region = models.CharField(max_length=100)  
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    picture = models.ImageField(blank=True, null=True)

    # def __str__(self):
    #     return f"{self.name} ({self.year})"

    class Meta:
        ordering = ['name']
