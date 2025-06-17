from .models import Ingresso
from rest_framework import viewsets
from .serializer import  IngressoSerializer
from django.shortcuts import render

# Create your views here.
class IngressoViewSet(viewsets.ModelViewSet):
    queryset = Ingresso.objects.all()
    serializer_class = IngressoSerializer  