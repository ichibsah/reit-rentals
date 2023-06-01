#from django.db import models
#from django import forms
from django.forms import ModelForm
from .myForms import Post, Newsletters


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["name", "email", "message"]

    def clean(self):
        super().clean()
        return self.cleaned_data


class NewsletterForm(ModelForm):
    class Meta:
        model = Newsletters
        fields = ["email"]

    def clean(self):
        super().clean()
        return self.cleaned_data