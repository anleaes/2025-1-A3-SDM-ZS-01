from .models import Filme
from rest_framework import viewsets
from .serializer import FilmeSerializer
from django.shortcuts import render

# Create your views here.

class FilmeViewSet(viewsets.ModelViewSet):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer  