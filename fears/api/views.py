from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import FearSerializer, FearCreateSerializer
from ..models import Fear

class FearViewSet(ModelViewSet):
	'''
	Model viewset for fears.
	'''

	serializer_class = FearSerializer
	queryset = Fear.objects.all()
	permission_classes = [IsAuthenticated,]
	serializer_action_classes = {
		'list' : FearSerializer,
		'create' : FearCreateSerializer,
	} 

	def get_serializer_class(self):
		try:
			return self.serializer_action_classes[self.action]
		except (KeyError, AttributeError):
			return super().get_serializer_class()

	def destroy(self, request, *args, **kwargs):
		instance = self.get_object()
		# Check if fear belong to logged in user
		if instance.user == request.user:
			self.perform_destroy(instance)
			return Response(status=status.HTTP_204_NO_CONTENT)
		return Response(status=status.HTTP_401_UNAUTHORIZED)



