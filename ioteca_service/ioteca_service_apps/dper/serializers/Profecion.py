from rest_framework import serializers
from ..models.Profecion import Profecion


class ProfecionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profecion
