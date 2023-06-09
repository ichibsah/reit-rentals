from django.views.generic import TemplateView
from django.shortcuts import render, HttpResponse
from .models import NewsletterForm, PostForm


class FormMixin:
    def save_form(self, form_class, request):
        """
        Saves the content of the form provided and returns the result
        """
        details = form_class(request.POST)
        if details.is_valid():
            post = details.save(commit=False)
            post.save()
            result = "Thank you"
            return HttpResponse(result, status=200)
        else:
            result = "Something went wrong. Please try again."
            return HttpResponse(result, status=400)


class HomeView(TemplateView):
    template_name = "home.html"


class DetailsView(TemplateView):
    template_name = "details.html"


class NewsletterView(FormMixin, TemplateView):
    template_name = "newsletter.html"

    def post(self, request, *args, **kwargs):
        return self.save_form(NewsletterForm, request)

    def get(self, request, *args, **kwargs):
        form = NewsletterForm(None)
        return render(request, 'newsletter.html', {'form': form})


class ContactView(FormMixin, TemplateView):
    template_name = "contact.html"

    def post(self, request, *args, **kwargs):
        return self.save_form(PostForm, request)

    def get(self, request, *args, **kwargs):
        form = PostForm(None)
        return render(request, 'contact.html', {'form': form})


class IndexView(FormMixin, TemplateView):
    template_name = "index.html"

    def post(self, request, *args, **kwargs):
        return self.save_form(PostForm, request)

    def get(self, request, *args, **kwargs):
        form = PostForm(None)
        return render(request, 'index.html', {'form': form})


class SignupView(FormMixin, TemplateView):
    template_name = "signup.html"

    def post(self, request, *args, **kwargs):
        return self.save_form(PostForm, request)

    def get(self, request, *args, **kwargs):
        form = PostForm(None)
        return render(request, 'signup.html', {'form': form})