from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage),
    path('blog/<slug:slug>', views.post)
]
