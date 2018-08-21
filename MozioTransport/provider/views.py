from django.shortcuts import render

# Create your views here.
from .models import Provider
from .serializers import ProviderSerializer
from rest_framework import generics


class ProviderList(generics.ListCreateAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class ProviderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
