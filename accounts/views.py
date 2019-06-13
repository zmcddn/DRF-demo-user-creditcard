from django.shortcuts import render

from rest_framework import viewsets, generics

from .serializers import CardSerializer
from .models import Card


class CardSerializerViewSet(viewsets.ModelViewSet):
    """
    Create Credit Card
    """

    queryset = Card.objects.all()
    serializer_class = CardSerializer