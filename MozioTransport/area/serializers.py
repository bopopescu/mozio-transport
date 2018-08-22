"""Area serializer class to make JSON REST API"""

from rest_framework import serializers
from rest_framework_cache.serializers import CachedSerializerMixin
from rest_framework_cache.registry import cache_registry

from .models import Area


class AreaSerializer(CachedSerializerMixin):
    # SlugRelatedField is to display name of provider instead of it id
    provider = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Area
        fields = ("name", "price", "provider", "poly")

cache_registry.register(AreaSerializer)
