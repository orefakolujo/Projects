from wsgiref.validate import validator
from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Review(models.Model):
    username = models.CharField(max_length=100)
    review = models.TextField(validators=[MinLengthValidator(5)])
    rating = models.IntegerField()

    def __str__(self):
        return f'{self.username}'
