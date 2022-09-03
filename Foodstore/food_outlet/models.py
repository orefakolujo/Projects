import imp
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

class Address(models.Model):
    street = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    postal = models.CharField(max_length=5)


    def __str__(self):
        return self.street
    

    
class Chef(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null= True)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    def full_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.full_name()


class Food(models.Model):
    name = models.CharField(max_length=30, null = True)
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE, null=True, related_name="foods")
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null=True)
    is_Sweet = models.BooleanField(default=True)
    slug = models.SlugField(default="", null=False, blank=True)

    def get_absolute_url(self):
        return reverse("details_page", args={self.slug})

    def __str__(self):
        return f'{self.name}'
