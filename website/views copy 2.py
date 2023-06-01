from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from django.core.mail import send_mail
from .import views
from django.shortcuts import HttpResponse, render, redirect
from django.http import JsonResponse
from pathlib import Path
import json
from .models import NewsletterForm

#from .forms import NameForm

# Create your views here.
class HomeView(TemplateView):
    template_name = "home.html"
    
class DetailsView(TemplateView):
    template_name = "details.html"
    
class NewsletterView(TemplateView):
    template_name = "newsletter.html"

    def post(self, request, *args, **kwargs):
        details = NewsletterForm(request.POST)
        if details.is_valid():
            post = details.save(commit=False)
            post.save()
            result = "Thank you"
            return HttpResponse(result, status=200)
        else:
            result = "Something went wrong. Please try again."
            return HttpResponse(result, status=400)
    
    def get(self, request, *args, **kwargs):
        form = NewsletterForm(None)
        return render(request, 'newsletter.html', {'form': form})
    
class ContactView(TemplateView):
    template_name = "contact.html"
    
    def post(self, request, *args, **kwargs):
        details = PostForm(request.POST)
        if details.is_valid():
            post = details.save(commit=False)
            post.save()
            result = "Thank you"
            return HttpResponse(result, status=200)
        else:
            result = "Something went wrong. Please try again."
            return HttpResponse(result, status=400)
    
    def get(self, request, *args, **kwargs):
        form = NewsletterForm(None)
        return render(request, 'contact.html', {'form': form})


class IndexView(TemplateView):
    template_name = "index.html"
    
    def post(self, request, *args, **kwargs):
        details = PostForm(request.POST)
        if details.is_valid():
            post = details.save(commit=False)
            post.save()
            result = "Thank you"
            return HttpResponse(result, status=200)
        else:
            result = "Something went wrong. Please try again."
            return HttpResponse(result, status=400)
    
    def get(self, request, *args, **kwargs):
        form = NewsletterForm(None)
        return render(request, 'index.html', {'form': form})    


class SignupView(TemplateView):
    template_name = "signup.html"
    
    def post(self, request, *args, **kwargs):
        details = PostForm(request.POST)
        if details.is_valid():
            post = details.save(commit=False)
            post.save()
            result = "Thank you"
            return HttpResponse(result, status=200)
        else:
            result = "Something went wrong. Please try again."
            return HttpResponse(result, status=400)
    
    def get(self, request, *args, **kwargs):
        form = NewsletterForm(None)
        return render(request, 'signup.html', {'form': form})  