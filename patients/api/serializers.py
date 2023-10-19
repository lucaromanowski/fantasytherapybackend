from rest_framework import serializers

from ..models import Patient


class PatientCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Patient
		fields = '__all__'


class PatientPrivateDetailsSerializer(serializers.ModelSerializer):
	'''
	This serializer is used for presenting patient details only for the patient himself. 
	'''
	class Meta:
		model = Patient
		fields = ('nickname','created')