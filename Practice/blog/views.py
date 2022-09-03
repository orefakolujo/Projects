
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
posts = {
    "slug": "this-is-it"
}


def homepage(request):
    return render(request, "blog/index.html")


def post(request, slug):
    return render(request, "blog/index.html", {
        
    })
