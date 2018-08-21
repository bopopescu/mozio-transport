from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Provider
from .serializers import ProviderSerializer

# Create your tests here.
class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_provider(name="", email="", phone_number="", language="", currency=""):
        if name != "" and email != "":
            Provider.objects.create(name=name, email=email,
                                    phone_number=phone_number, language=language, currency=currency)

    def setUp(self):
        self.create_provider("Mozio1", "admin@mozio.com", "+999999999", "en", "2000.2")
        self.create_provider("Mozio2", "admin2@mozio.com", "+123456789", "en", "5000.6")



class ProviderTest(BaseViewTest):

    def test_getting_all_providers(self):
        response = self.client.get(reverse('providers-list'))
        expected = Provider.objects.all()
        serialized = ProviderSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_creating_provider(self):
        self.assertEqual(Provider.objects.count(), 2)

    def test_get_single_provider(self):
        response = self.client.get(
            reverse('providers-detail', kwargs={'pk': 2}))
        expected = Provider.objects.get(pk=2)
        serializer = ProviderSerializer(expected)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_updating_provider(self):
        response = self.client.put(reverse('providers-detail', kwargs={'pk': 1}), {
            'name': 'Mozio1111',
            'email': 'admin1111@mozio.com',
            'phone_number': '+999999999',
            'language' : 'en',
            'currency' : 2000.2
        }, format="json")
        expected = Provider.objects.get(pk=1)
        serializer = ProviderSerializer(expected)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deleting_provider(self):
        response = self.client.delete(reverse('providers-detail', kwargs={'pk': 1}))
        self.assertEqual(204, response.status_code)

    def test_get_invalid_provider(self):
        response = self.client.get(
            reverse('providers-detail', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
