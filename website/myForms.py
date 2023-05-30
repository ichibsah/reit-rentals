
from django.forms import ModelForm
from django import forms
from .models import *

from django.db import models

# model named Post
class Post(models.Model):

	# define a username field with bound max length it can have
	name = models.TextField(blank = False, null = False)
	
	# This is used to write a post
	email = models.EmailField(blank = False, null = False, unique=True)
	
	# Values for gender are restricted by giving choices
	message = models.TextField(blank = False, null = False)
	
	time = models.DateTimeField(auto_now_add = True)
	#id = models.PositiveIntegerField(primary_key=True, unique=True, auto_created=True)
	ipaddress = models.GenericIPAddressField(auto_created=True, null = True )
