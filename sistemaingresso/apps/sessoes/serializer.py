from .models import Sessao
from rest_framework import serializers

class SessaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sessao
        fields = '__all__'