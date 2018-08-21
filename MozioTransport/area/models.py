from django.contrib.gis.db import models

# Create your models here.
from provider.models import Provider
from django.core.validators import RegexValidator


class Area(models.Model):
    name = models.CharField(max_length=250)
    price = models.IntegerField()
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, null=True)

    coordinate_regex = RegexValidator(regex=r'^\d+\.\d+$',
                                 message="Please enter a decimal number.")
    longitude = models.CharField(validators=[coordinate_regex], max_length=50, blank=True)
    latitude = models.CharField(validators=[coordinate_regex], max_length=50, blank=True)
    poly = models.PolygonField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'areas'
