from rest_framework import serializers
from ..models import Monster

class MonsterCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monster 
        fields = ('name', 'patient',)