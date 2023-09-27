from rest_framework import serializers

from ..models import PatientTherapistRelationship


class CreateTherapistToPatientRelationshipSerializer(serializers.ModelSerializer):
	class Meta:
		model = PatientTherapistRelationship
		fields = ('therapist', 'patient',)