""" Area model to manage service areas polygons

This model has attributes
    - name : name of service area polygon
    - price : price of service area polygon
    - provider : provider corresponding to that area. It's a foreign key
    - poly : service area of transportation supplier represents by a polygon form
"""
from django.contrib.gis.db import models

from provider.models import Provider


class Area(models.Model):
    name = models.CharField(max_length=250)
    price = models.IntegerField()
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, null=True)
    poly = models.PolygonField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'areas'
