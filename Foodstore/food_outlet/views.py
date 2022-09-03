from django.shortcuts import render, get_object_or_404
from .models import Food

# Create your views here.

def index(request):
    food = Food.objects.all().order_by("name")
    return render(request, "food_outlet/index.html", {
        "food": food,
    })


def details_page(request, slug):
    foods = Food.objects.get(slug=slug)
    return render(request, "food_outlet/details.html", {
        "chef": foods.chef,
        "name": foods.name,
        "rating": foods.rating,
        "is_sweet": foods.is_Sweet,
    })
