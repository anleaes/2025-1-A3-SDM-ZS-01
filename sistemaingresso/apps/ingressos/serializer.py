from .models import Ingresso
from rest_framework import serializers
    
class IngressoSerializer(serializers.ModelSerializer):
    sessao_details = serializers.StringRelatedField(source='sessao', read_only=True)
    cadeira_details = serializers.StringRelatedField(source='cadeira', read_only=True)

    class Meta:
        model = Ingresso
        fields = '__all__'

        extra_kwargs = {
            'sessao': {'write_only': True},
            'cadeira': {'write_only': True}
        }