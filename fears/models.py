from django.conf import settings 
from django.db import models
from django.utils.text import slugify


class Fear(models.Model):
	'''
	Fear model. 
	'''
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='fears', on_delete=models.CASCADE)
	title = models.CharField(max_length = 200)
	slug = models.SlugField(unique=True, blank=True)
	description = models.TextField(default='')

	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True) 

	def __str__(self):
		return str(self.title)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		super(Fear, self).save(*args, **kwargs)


class FearIntensity(models.Model):
	'''
	Fear intensity model. Levels: low, medium, high. Basic way of measuring fear level at given time. 
	'''

	INTENSITY_LEVELS = [
		('10', 'Low'),
		('20', 'Medium'),
		('30', 'High'),
	]

	fear = models.ForeignKey(Fear, related_name='fear_intensities', on_delete=models.CASCADE)
	intensity_level = models.CharField(max_length=2, choices=INTENSITY_LEVELS, default='10')
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True) 




	