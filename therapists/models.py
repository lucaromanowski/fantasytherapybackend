from django.conf import settings 
from django.db import models
from django.utils.text import slugify


class Therapist(models.Model):
	'''
	This is a therapist model.
	'''
	user 		= models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	first_name 	= models.CharField(max_length=120)
	last_name 	= models.CharField(max_length=120)
	
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True) 


	def __str__(self):
		return f'{self.first_name} {self.last_name}'

