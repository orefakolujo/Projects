from django.urls import path
from . import views

urlpatterns = [
    path("", views.signup),
    path("thank-you", views.thankYou)
]
