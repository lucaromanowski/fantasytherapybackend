from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView

from .serializers import PatientRegistrationSerializer, TherapistRegistrationSerializer
from ..models import CustomUser



class PatientRegistrationAPIView(CreateAPIView):
	'''
	This view creates and combine custom user and patient instances.
	Required fields: email, password, password2, nickname(nickname can be changed after registration)
	'''
	permissions_classes = (AllowAny,)
	serializer_class = PatientRegistrationSerializer
	queryset = CustomUser.objects.all()

class TherapistRegistrationAPIView(CreateAPIView):
	'''
	This view creates and combine custom user and therapist instances.
	Required fields: email, password, password2, first_name, last_name.
	'''
	permissions_classes = (AllowAny,)
	serializer_class = TherapistRegistrationSerializer
	queryset = CustomUser.objects.all()
