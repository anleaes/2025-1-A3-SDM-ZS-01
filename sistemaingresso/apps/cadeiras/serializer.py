from .models import Cadeira
from rest_framework import serializers

class CadeiraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cadeira
        fields = '__all__'