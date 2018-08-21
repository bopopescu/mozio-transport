# Create your views here.
from .models import Area
from .serializers import AreaSerializer
from rest_framework import generics
from decimal import Decimal


class AreaList(generics.ListCreateAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


class AreaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

class AreaListCoord(generics.ListAPIView):
    serializer_class = AreaSerializer

    def get_queryset(self, *args, **kwargs):
        """ This view should return a list of polygons matching same latitude and longitude"""
        lat =  str(self.kwargs['lati'])
        lng = str(self.kwargs['lngi'])
        return Area.objects.filter(latitude=lat, longitude=lng)
