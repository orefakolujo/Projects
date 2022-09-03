from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import reviewForm

# Create your views here.

def review(request):
    if request.method == 'POST':
       form = reviewForm(request.POST)
       
       if form.is_valid():
        form.save()
        return HttpResponseRedirect("/thank-you")

    else:
        form = reviewForm()
    
    return render(request, "reviews/review.html", {
        "form": form,
    })

def thankYou(request):
    return render(request, "reviews/thank-you.html")