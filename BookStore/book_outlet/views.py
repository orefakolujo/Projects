
from multiprocessing import AuthenticationError
from pickletools import read_int4
from turtle import title
from django.shortcuts import get_object_or_404, render
from .models import Book
from django.http import Http404
from django.db.models import Avg

# Create your views here.


def index(request):
    books = Book.objects.all().order_by("title")
    total_books = books.count()
    average = books.aggregate(Avg("rating"))

    return render(request, "book_outlet/index.html", {
        "book": books,
        "total": total_books,
        "averagerating": average
    })


def book_details(request, slug):

    book = get_object_or_404(Book, slug=slug)
    return render(request, "book_outlet/book_detail.html", {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "isBestselling": book.is_Bestselling,
    })
