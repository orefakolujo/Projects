from dataclasses import field
from django import forms

from reviews.models import Review
from .models import Review

# class reviewForm(forms.Form):
#     username = forms.CharField(label="Your Name", max_length=100, error_messages={
#         "required": "Please enter your name",
#         "max_length": "Your name is too long"
#     })

#     review = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=100)
#     rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)

class reviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        labels = {
            "username": "Your Name",
            "review": "Your Feedback",
            "rating": "Your Rating"
        }

        error_messages = {
            "username": {
                "required": "Please enter your name",
                "max_length": "Your name is too long"
            },

            "review":{
                "min_length": "Your feedback is too short"
            }
        }