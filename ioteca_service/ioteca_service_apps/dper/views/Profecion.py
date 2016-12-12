from rest_framework import serializers, viewsets
from django.db.models import Q
from operator import __or__ as OR
from functools import reduce
from ..serializers.Profecion import ProfecionSerializer
from ..models.Profecion import Profecion


class ProfecionViewSet(viewsets.ModelViewSet):
    queryset = Profecion.objects.all()
    serializer_class = ProfecionSerializer
