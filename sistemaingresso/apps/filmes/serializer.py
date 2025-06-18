from .models import Filme
from rest_framework import serializers

class FilmeSerializer(serializers.ModelSerializer):
    generos = serializers.StringRelatedField(many=True)

    class Meta:
        model = Filme
        fields = '__all__'