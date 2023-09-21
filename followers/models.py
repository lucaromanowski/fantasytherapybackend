from django.db import models

from therapists.models import Therapist
from patients.models import Patient

class PatientTherapistConnection(models.Model):
	'''
	This model represents therapist-patient connection. 
	Only therapist can initiate it.
	Patient accepts it.
	'''


	therapist = models.ForeignKey(Therapist, related_name='following', on_delete=models.CASCADE)
	patient = models.ForeignKey(Patient, related_name='follower', on_delete=models.CASCADE)

	isPatientAccepting = models.BooleanField(default=False)

	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True) 


	class Meta:
		unique_together = ('therapist', 'patient')

	def __str__(self):
		return f'Connection between therapist {self.therapist} and patient {self.patient}'



