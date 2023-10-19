from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

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


class CustomAuthToken(ObtainAuthToken):
	'''
	This view adds some additional information to auth token response. 
	'''
	
	def post(self, request, *args, **kwargs):
		serializer = self.serializer_class(data=request.data, context={'request':request})
		serializer.is_valid(raise_exception=True)
		user = serializer.validated_data['user']
		token, created = Token.objects.get_or_create(user=user)
		return Response({
			'token': token.key,
			'user_id': user.pk,
		})


