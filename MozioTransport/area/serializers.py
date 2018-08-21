from rest_framework import serializers
from .models import Area
from provider.models import Provider


class AreaSerializer(serializers.ModelSerializer):
    provider = serializers.SlugRelatedField(read_only=True,slug_field='name')

    class Meta:
        model = Area
        fields = ("name", "price", "provider", "longitude", "latitude", "poly")
