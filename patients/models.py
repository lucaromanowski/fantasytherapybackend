from django.conf import settings
from django.db import models
from django.utils.text import slugify


from therapists.models import Therapist
from fears.models import Fear


class Patient(models.Model):
	'''
	This model represents data of the patient. 
	'''
	user 		= models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	first_name 	= models.CharField(max_length=80, blank=True)
	last_name 	= models.CharField(max_length=80, blank=True)
	
	fears		= models.ForeignKey(Fear, related_name='patients', on_delete=models.CASCADE, null=True, blank=True)
	nickname 	= models.CharField(max_length=120)
	#slug = models.SlugField(unique=True, blank=True)
	

	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True) 

	class Meta:
		ordering = ['updated',]

	def __str__(self):
		return f'{self.nickname}'
