from django.shortcuts import render
from .models import Sessao
from rest_framework import viewsets
from .serializer import SessaoSerializer
from django.shortcuts import render

# Create your views here.

class SessaoViewSet(viewsets.ModelViewSet):
    queryset = Sessao.objects.all()
    serializer_class = SessaoSerializer  