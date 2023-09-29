from rest_framework import serializers

from ..models import Fear, FearIntensity 
from accounts.api.serializers import CustomUserSerializer


class FearIntensitySerializer(serializers.ModelSerializer):
	class Meta:
		model = FearIntensity 
		fields = ['intensity_level', 'created', 'updated',]


class FearSerializer(serializers.ModelSerializer):
	'''
	Fear serializer.
	'''
	user = CustomUserSerializer()
	fear_intensities = FearIntensitySerializer(many=True, read_only=True)

	class Meta:
		model = Fear
		fields = ['id', 'fear_intensities', 'user', 'title', 'description', 'created', 'updated',]


class FearCreateSerializer(serializers.ModelSerializer):
	user = serializers.HiddenField(default=serializers.CurrentUserDefault())

	class Meta:
		model = Fear
		fields = ('user', 'title', 'description',)



