from .models import Genero
from rest_framework import viewsets
from .serializer import GeneroSerializer
from django.shortcuts import render

# Create your views here.

class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer  