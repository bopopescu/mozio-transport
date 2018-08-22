""" API Root view to return a 200_OK response for url path '/' """

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def api_root(request):
    return Response(status=status.HTTP_200_OK)
