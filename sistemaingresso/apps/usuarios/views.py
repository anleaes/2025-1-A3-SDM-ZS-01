from .models import Usuario
from rest_framework import viewsets
from .serializer import UsuarioSerializer
from django.shortcuts import render

# Create your views here.

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer  
