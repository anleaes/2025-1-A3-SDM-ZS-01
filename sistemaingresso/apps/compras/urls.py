from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'compras'

router = routers.DefaultRouter()
router.register('', views.CompraViewSet, basename='compras')

urlpatterns = [
    path('', include(router.urls) )
]