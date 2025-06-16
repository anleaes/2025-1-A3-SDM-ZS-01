from django.urls import path, include
from . import views
from rest_framework import routers


app_name = 'filmes'

router = routers.DefaultRouter()
router.register('', views.FilmeViewSet, basename='Filmes')

urlpatterns = [
    path('', include(router.urls) )
]