from rest_framework import serializers
from ..models.Persona import Persona


class PersonaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Persona
