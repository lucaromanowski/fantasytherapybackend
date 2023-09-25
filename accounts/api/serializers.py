from rest_framework import serializers

from django.contrib.auth.password_validation import validate_password

from ..models import CustomUser
from patients.models import Patient
from therapists.models import Therapist

class CustomUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomUser
		fields =['email',]


print('WARNING! Do not leak email adress like in CustomUserSerializer.')


class PatientRegistrationSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True, required=True, validators=[validate_password,])
	password2 = serializers.CharField(write_only=True, required=True)

	nickname = serializers.CharField(write_only=True)

	class Meta:
		model = CustomUser
		fields = ['email', 'password', 'password2','nickname',]

	def validate(self, attrs):
		if attrs['password'] != attrs['password2']:
			raise serializers.ValidationError({'password': "Password fields didn't match"})
		return attrs

	def create(self, validated_data):
		user = CustomUser.objects.create(
			email = validated_data['email'],
		)

		# Create patient
		Patient.objects.create(user=user, nickname=validated_data['nickname'])

		user.set_password(validated_data['password'])
		user.save()
		return user


class TherapistRegistrationSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True, required=True, validators=[validate_password,])
	password2 = serializers.CharField(write_only=True, required=True)

	first_name = serializers.CharField(write_only=True, required=True)
	last_name = serializers.CharField(write_only=True, required=True)


	class Meta:
		model = CustomUser
		fields = ['email', 'password', 'password2', 'first_name', 'last_name',]

	def validate(self, attrs):
		if attrs['password'] != attrs['password2']:
			raise serializers.ValidationError({'password': "Password fields didn't match"})
		return attrs

	def create(self, validated_data):
		user = CustomUser.objects.create(
			email = validated_data['email'],
		)


		# Create patient
		Therapist.objects.create(user=user, first_name=validated_data['first_name'], last_name=validated_data['last_name'])

		user.set_password(validated_data['password'])
		user.save()
		return user







