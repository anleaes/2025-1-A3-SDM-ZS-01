from .models import Compra
from rest_framework import serializers

class CompraSerializer(serializers.ModelSerializer):
    usuario_nome = serializers.CharField(source='usuario.nome', read_only=True)
    class Meta:
        model = Compra
        fields = '__all__'