from django.urls import path, include
from . import views
from rest_framework import routers


app_name = 'sessoes'

router = routers.DefaultRouter()
router.register('', views.SessaoViewSet, basename='sessoes')

urlpatterns = [
    path('', include(router.urls) )
]