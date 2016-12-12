from django.conf.urls import url, include
from rest_framework import routers
from .views.Profecion import ProfecionViewSet
from .views.Persona  import PersonaViewSet

router = routers.DefaultRouter()
router.register(r'Profeciones', ProfecionViewSet)
router.register(r'Personas', PersonaViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
