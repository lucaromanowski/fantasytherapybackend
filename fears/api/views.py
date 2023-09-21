from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import FearSerializer
from ..models import Fear

class FearViewSet(ModelViewSet):
	'''
	Model viewset for fears.
	'''

	serializer_class = FearSerializer
	queryset = Fear.objects.all()


