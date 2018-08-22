"""Provider view using Django Rest Framework generics
in order to have fast built in CRUD operation and generate response in JSON
"""
from rest_framework import generics

from .models import Provider
from .serializers import ProviderSerializer


class ProviderList(generics.ListCreateAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class ProviderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
