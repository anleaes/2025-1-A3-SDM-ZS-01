from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'ingressos'

router = routers.DefaultRouter()
router.register('', views.IngressoViewSet, basename='ingressos')

urlpatterns = [
    path('', include(router.urls) )
]