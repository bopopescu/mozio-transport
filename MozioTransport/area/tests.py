"""Area test Class
This class contains area tests driven cases to :
    - get all areas
    - create new area
    - get single area
    - update area
    - delete area
    - get invalid area
"""

from django.urls import reverse

from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status

from provider.models import Provider
from .models import Area
from .serializers import AreaSerializer


class BaseAreaTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_area(name="", price=0, provider=0, poly=[]):
        if name != "" and price != 0:
            Area.objects.create(name=name, price=price, provider=provider, poly=poly)

    def create_provider(name="", email="", phone_number="", language="", currency=""):
        if name != "" and email != "":
            Provider.objects.create(name=name, email=email, phone_number=phone_number,
                                    language=language, currency=currency)

    def setUp(self):
        self.create_provider("Mozio1", "admin@mozio.com", "+999999999", "en", "2000.2")
        self.create_provider("Mozio2", "admin2@mozio.com", "+123456789", "en", "5000.6")
        p1 = Provider.objects.get(pk=1)
        p2 = Provider.objects.get(pk=2)
        self.create_area("Area1", 15200, p1.pk, [[12.41, 43.95], [12.45, 43.97], [12.41, 43.95]])
        self.create_area("Area2", 9000, p2.pk, [[18.69, 12.36], [12.05, 29.78], [18.69, 12.36]])
        self.create_area("Area3", 20000, p1.pk, [[80.69, 58.58], [23.87, 62.39], [80.69, 58.58]])


class AreaTest(BaseAreaTest):

    def test_getting_all_areas(self):
        response = self.client.get(reverse('areas-list'))
        expected = Area.objects.all()
        serialized = AreaSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_creating_area(self):
        self.assertEqual(Area.objects.count(), 3)

    def test_get_single_area(self):
        response = self.client.get(
            reverse('areas-detail', kwargs={'pk': 2}))
        expected = Area.objects.get(pk=2)
        serializer = AreaSerializer(expected)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_updating_area(self):
        response = self.client.put(reverse('areas-detail', kwargs={'pk': 1}), {
            'name': 'Area111',
            'price': 15200,
            'provider': 2,
            'poly': [[12.41, 43.95], [12.45, 43.97], [12.41, 43.95]]
        }, format="json")
        expected = Area.objects.get(pk=1)
        serializer = AreaSerializer(expected)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deleting_area(self):
        response = self.client.delete(reverse('areas-detail', kwargs={'pk': 1}))
        self.assertEqual(204, response.status_code)

    def test_get_invalid_area(self):
        response = self.client.get(
            reverse('areas-detail', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
