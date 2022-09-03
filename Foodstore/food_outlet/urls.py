from . import views
from django.urls import path

urlpatterns = [
    path("", views.index),
    path("<slug:slug>", views.details_page, name="details_page")
]


