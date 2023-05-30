
#from django.forms import ModelForm
#from django import forms
#from .models import *
from django.db import models

# model named Post
class Newsletters(models.Model):

	# This is used to write a post
	email = models.EmailField(blank = False, null = False, unique=True)
	
	time = models.DateTimeField(auto_now_add = True)

	ipaddress = models.GenericIPAddressField(auto_created=True, null = True )
