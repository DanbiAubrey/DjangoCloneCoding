from django.db import models

# Create your models here.
# Description of the shape of the data in the app

class House(models.Model): 
    """ Model Definition for Houses """
    name = models.CharField(max_length=140)
    price_per_night = models.PositiveIntegerField(verbose_name="Price", help_text="Positive Numbers Only")
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(default=True, help_text="Does this house allow pets?", verbose_name="Pets Allowed?")

    def __str__(self):
        return self.name