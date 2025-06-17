from .models import Itemcompra
from rest_framework import serializers
    
class ItemcompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Itemcompra
        fields = '__all__'