from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'itemcompras'

router = routers.DefaultRouter()
router.register('', views.ItemCompraViewSet, basename='itens_compra')

urlpatterns = [
    path('', include(router.urls) )
]