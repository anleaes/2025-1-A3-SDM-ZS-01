from .models import Itemcompra
from rest_framework import serializers
    
class ItemcompraSerializer(serializers.ModelSerializer):
    compra_details = serializers.StringRelatedField(source='compra', read_only=True)
    ingresso_details = serializers.StringRelatedField(source='ingresso', read_only=True)
    
    class Meta:
        model = Itemcompra
        fields = '__all__'