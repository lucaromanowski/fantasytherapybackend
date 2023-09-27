from rest_framework.permissions import BasePermission
from django.core.exceptions import ObjectDoesNotExist


class IsTherapistPermission(BasePermission):
	'''
	Only therapist permission.
	'''
	
	def has_permission(self, request, view):
		try:
			# Attempt to access the related object
			related_object = request.user.therapist # Replace with your actual code
		except ObjectDoesNotExist:
			# Handle the case where the related object does not exist
			return False
		return True