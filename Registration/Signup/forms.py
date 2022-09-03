import email
from django import forms

class SignupForm(forms.Form):
    firstname = forms.CharField(max_length=100, label="Your Firstname", error_messages={
        "required": "This field must not be empty",
    })
    lastname = forms.CharField(label="Lastname")
    email = forms.EmailField(label="Email")