from django.contrib import admin
from django.urls import path, include
from .views import UserViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('usuarios', UserViewSet, basename='Usuario')

urlpatterns = [
    path('', include(router.urls)),
]
