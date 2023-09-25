from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView

from .serializers import PatientRegistrationSerializer
from ..models import CustomUser



class PatientRegistrationAPIView(CreateAPIView):
	permissions_classes = (AllowAny,)
	serializer_class = PatientRegistrationSerializer
	queryset = CustomUser.objects.all()

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		headers = self.get_success_headers(serializer.data)		
		return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class TherapistRegistrationAPIView():
	pass