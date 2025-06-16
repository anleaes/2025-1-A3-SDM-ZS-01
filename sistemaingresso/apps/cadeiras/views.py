from .models import Cadeira
from rest_framework import viewsets
from .serializer import CadeiraSerializer
from django.shortcuts import render

# Create your views here.

class CadeiraViewSet(viewsets.ModelViewSet):
    queryset = Cadeira.objects.all()
    serializer_class = CadeiraSerializer  