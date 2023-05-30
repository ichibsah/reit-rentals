from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from django.core.mail import send_mail
from .import views
from django.shortcuts import HttpResponse, render, redirect
from django.http import JsonResponse

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
            #return JsonResponse({'status': 'failed', 'errors': details.errors})
            return JsonResponse({'status': 'success'})
            #return render(request, "newsletter.html", {'mSentSucess':'data submitted successfully'})
            #return HttpResponse({'mSentSuccess': 'data submitted successfully'})
        else:
            #return render(request, "newsletter.html", {'form': details})
            #return JsonResponse({'status': 'failed', 'errors': details.errors}) #Debug
            return JsonResponse({'status': 'failed'})
    
    def get(self, request, *args, **kwargs):
        form = NewsletterForm(None)
        return render(request, 'newsletter.html', {'form': form})
    
    
class ContactView(TemplateView):
    template_name = "contact.html"


class IndexView(TemplateView):
    template_name = "index.html"
        



def signupform(request):

	# check if the request is post
	if request.method =='POST':

		# Pass the form data to the form class
		details = PostForm(request.POST)

		# In the 'form' class the clean function
		# is defined, if all the data is correct
		# as per the clean function, it returns true
		if details.is_valid():

			# Temporarily make an object to be add some
			# logic into the data if there is such a need
			# before writing to the database
			post = details.save(commit = False)

			# Finally write the changes into database
			post.save()

			# redirect it to some another page indicating data
			# was inserted successfully
			#return HttpResponse("data submitted successfully")
			return HttpResponse({'mSentSucess':'data submitted successfully'})
            #return render(request, "signup.html", {'mSentSucess':'data submitted successfully'})
			
		else:
		
			# Redirect back to the same page if the data
			# was invalid
			return render(request, "signup.html", {'form':details})
	else:

		# If the request is a GET request then,
		# create an empty form object and
		# render it into the page
		form = PostForm(None)
		return render(request, 'signup.html', {'form':form})
