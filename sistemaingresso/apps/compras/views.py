from .models import Compra
from rest_framework import viewsets
from .serializer import CompraSerializer
from django.shortcuts import render

# Create your views here.

class CompraViewSet(viewsets.ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer  