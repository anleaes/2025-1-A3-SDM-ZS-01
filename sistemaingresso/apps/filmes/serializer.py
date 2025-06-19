from .models import Filme
from generos.models import Genero
from rest_framework import serializers

class FilmeSerializer(serializers.ModelSerializer):
    generos = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Filme
        fields = '__all__'
    
    extra_kwargs = {
            'generos': {'write_only': True}
        }