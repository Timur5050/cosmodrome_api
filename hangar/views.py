from hangar.serializers import FeatureSerializer
from hangar.models import Feature

from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet


class FeatureViewSet(ModelViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
