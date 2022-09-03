from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import SignupForm
# Create your views here.

def signup(request):
    
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect('thank-you')

    else:
        form = SignupForm()

    return render(request, "signup/signup.html", {
        "form": form,
    })

def thankYou(request):
    return render(request, 'signup/thankyou.html')