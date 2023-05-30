from django.db import models
from django import forms
from django.core import validators
from .myForms import *
from .newsletters import *
from pathlib import Path
from django.forms import ModelForm
from django import forms
from .models import *


# define the class of a form
class PostForm(ModelForm):
	class Meta:
		# write the name of models for which the form is made
		model = Post	

		# Custom fields
		fields =["name", "email", "message"]

	# this function will be used for the validation
	def clean(self):

		# data from the form is fetched using super function
		super(PostForm, self).clean()
		
		# extract the username and text field from the data
		name = self.cleaned_data.get('name')
		email = self.cleaned_data.get('email')
		message = self.cleaned_data.get('message')

		# conditions to be met for the username length
		# if len(username) < 5:
		# 	self.errors(['username'] = self.error_class([
		# 		'Minimum 5 characters required']))
		# if len(text) <10:
		# 	self.errors['text'] = self.error_class([
		# 		'Post Should Contain a minimum of 10 characters'])

		# return any errors if found
		return self.cleaned_data
    

class NewsletterForm(ModelForm):
	class Meta:
		# write the name of models for which the form is made
		model = Newsletters	

		# Custom fields
		fields =["email"]

	# this function will be used for the validation
	def clean(self):

		# data from the form is fetched using super function
		super(NewsletterForm, self).clean()
		
		# extract the username and text field from the data
		email = self.cleaned_data.get('email')

		return self.cleaned_data
    