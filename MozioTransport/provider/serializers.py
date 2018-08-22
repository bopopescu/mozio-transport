"""Provider serializer class to make JSON REST API"""

from rest_framework import serializers
from rest_framework_cache.serializers import CachedSerializerMixin
from rest_framework_cache.registry import cache_registry

from .models import Provider


class ProviderSerializer(CachedSerializerMixin):
    class Meta:
        model = Provider
        fields = ("name", "email", "phone_number", "language", "currency")

cache_registry.register(ProviderSerializer)
