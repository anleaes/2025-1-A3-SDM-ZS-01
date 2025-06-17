from .models import Itemcompra
from rest_framework import viewsets
from .serializer import  ItemcompraSerializer
from django.shortcuts import render

# Create your views here.

class ItemCompraViewSet(viewsets.ModelViewSet):
    queryset = Itemcompra.objects.all()
    serializer_class = ItemcompraSerializer  