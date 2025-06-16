from django.urls import path, include
from . import views
from rest_framework import routers


app_name = 'cadeiras'

router = routers.DefaultRouter()
router.register('', views.CadeiraViewSet, basename='Cadeiras')

urlpatterns = [
    path('', include(router.urls) )
]