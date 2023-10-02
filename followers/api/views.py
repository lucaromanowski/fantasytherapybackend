from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from patients.models import Patient
from utils.permissions import IsTherapistPermission
from .serializers import CreateTherapistToPatientRelationshipSerializer


class CreatTerapistToPatientRelationshipAPIView(CreateAPIView):
	'''
	IsTherapistPermission checks if user is a therapist. Only therapist can create this relationship.
	'''
	serializer_class = CreateTherapistToPatientRelationshipSerializer
	permission_classes = [IsAuthenticated, IsTherapistPermission,]

	def create(self, request, *args, **kwargs):
		patient = get_object_or_404(Patient, id=request.data.get('patient_id'))

		data = {
			'therapist': request.user.therapist.pk,
			'patient': patient.pk,
		}

		serializer = self.get_serializer(data=data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		headers = self.get_success_headers(serializer.data)
		return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
