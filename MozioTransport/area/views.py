"""Area view using Django Rest Framework generics
in order to have fast built in CRUD operation and generate response in JSON

When latitude and longitude are provided in URL pattern, queryset method searches
all polygon which contain the point defined by latitude and longitude provided in URL parameters.
In other words, AreaListCoord class creates a GEOS Point object as Point(lat,long)
and then checks if that point is within a Polygon area.
"""

from django.contrib.gis.geos import GEOSGeometry

from rest_framework import generics

from .models import Area
from .serializers import AreaSerializer


class AreaList(generics.ListCreateAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


class AreaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


class AreaListCoord(generics.ListAPIView):
    serializer_class = AreaSerializer

    def get_queryset(self, *args, **kwargs):
        lat = self.kwargs['lati']
        lng = self.kwargs['lngi']
        list_area = Area.objects.all()
        tab = []
        # Convert latitude and longitude in a GEOS Point
        coordinates = 'SRID=32140;POINT('+str(lat)+' '+str(lng)+')'
        for i in range(len(list_area)):
            elem = list_area[i].poly
            polygo = GEOSGeometry(elem)
            point = GEOSGeometry(coordinates)
            # Check if the Point is within a Polygon area
            if polygo.contains(point):
                tab.append(list_area[i].pk)
        return Area.objects.filter(pk__in=tab)
