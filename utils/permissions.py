from django.shortcuts import get_object_or_404

from rest_framework.permissions import BasePermission
from django.core.exceptions import ObjectDoesNotExist

from therapists.models import Therapist
from patients.models import Patient

class IsPatientPermission(BasePermission):
	'''
	Only therapist permission.
	'''
	
	def has_permission(self, request, view):
		try:
			# Attempt to access the related object
			related_object = request.user.patient 
		except ObjectDoesNotExist:
			# Handle the case where the related object does not exist
			return False
		return True


class IsTherapistPermission(BasePermission):
	'''
	Only therapist permission.
	'''
	
	def has_permission(self, request, view):
		try:
			# Attempt to access the related object
			related_object = request.user.therapist 
		except ObjectDoesNotExist:
			# Handle the case where the related object does not exist
			return False
		return True

class IsTherapistOfPatientPermission(BasePermission):
	'''
	This permission checks if the patient has a relationship with a therapist
	anf if the patien accepted this relationship.
	'''
	def has_permission(self, request, view):
		# Get Patient and Therapist
		therapist = request.user.therapist

		# Patient pk was sent in the url as a lookup kwarg e.g. 'https://(...)/something/anotherthing/16' - mothod GET
		if view.kwargs.get('pk') != None:
			patient = get_object_or_404(Patient, pk=view.kwargs.get('pk'))
		
		# Patient pk was sent as patient property in request.data -  method POST
		elif request.data.get('patient') != None:
			patient = get_object_or_404(Patient, pk=request.data.get('patient'))
		else:
			patient = get_object_or_404(Patient, pk=view.kwargs.get('pk'))

		# Chech if the Therapist is taking care of the Patient and if the Patient accepted it.
		if therapist.following.filter(patient=patient).exists() and therapist.following.filter(patient=patient)[0].isPatientAccepting:			
			return True
		return False