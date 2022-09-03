from datetime import date
from tkinter import image_names
from turtle import title
from django.db import models
from django.utils.text import slugify
from django.core.validators import MinLengthValidator

# Create your models here.

class Author(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

    def full_name(self):
        return self.firstname + " " + self.lastname
    
    def __str__(self):
        return self.full_name()

class Tag(models.Model):
    caption = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.caption}'
    

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name="posts", null=True)
    excerpt = models.CharField(max_length=300)
    image_name = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, default = "", null= False, blank=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return f'{self.title}'

