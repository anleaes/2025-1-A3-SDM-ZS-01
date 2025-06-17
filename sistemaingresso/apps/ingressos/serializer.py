from .models import Ingresso
from rest_framework import serializers
    
class IngressoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingresso
        fields = '__all__'