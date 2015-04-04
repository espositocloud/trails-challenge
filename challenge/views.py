from django.shortcuts import render
from rest_framework import viewsets

from .models import Group, Technique, Patrol, Test
from .serializers import GroupSerializer, TechniqueSerializer, PatrolSerializer, TestSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allow groups to be viewed.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class TechniqueViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allow techniques to be viewed.
    """
    queryset = Technique.objects.all()
    serializer_class = TechniqueSerializer


class PatrolViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allow patrols to be viewed.
    """
    queryset = Patrol.objects.all()
    serializer_class = PatrolSerializer


class TestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allow tests to be viewed.
    """
    queryset = Test.objects.all()
    serializer_class = TestSerializer
