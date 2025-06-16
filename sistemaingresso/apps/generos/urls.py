from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'generos'

router = routers.DefaultRouter()
router.register('', views.GeneroViewSet, basename='Generos')

urlpatterns = [
    path('', include(router.urls) )
]