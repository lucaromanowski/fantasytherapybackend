from rest_framework import serializers

from ..models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomUser
		fields =['email',]


print('WARNING! Do not leak email adress like in CustomUserSerializer.')