from rest_framework import serializers, viewsets
from django.db.models import Q
from operator import __or__ as OR
from functools import reduce
from ..serializers.Persona import PersonaSerializer
from ..models.Persona import Persona


class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
