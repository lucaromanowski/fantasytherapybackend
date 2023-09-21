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



	fears		= models.ForeignKey(Fear, related_name='patients', on_delete=models.CASCADE, null=True, blank=True)
	


	nickname = models.CharField(max_length=120)
	slug = models.SlugField(unique=True, blank=True)

	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True) 

	def __str__(self):
		return f'{self.nickname}'

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.nickname)
		super(Patient, self).save(*args, **kwargs)