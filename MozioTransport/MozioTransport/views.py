
from rest_framework.decorators import api_view # new
from rest_framework.response import Response # new





@api_view(['GET']) # new
def api_root(request, format=None):
    return Response({

    })
