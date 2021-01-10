from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from app.models import City, Location, State
from app.serializers import CitySerializer, LocationSerializer, StateSerializer


class CityApiTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.city_1 = City.objects.create(name='Москва')
        cls.city_2 = City.objects.create(name='Санкт-Петербург')

    def test_get(self):
        url = reverse('city-detail', kwargs={'pk': self.city_1.id})
        serialized_data = CitySerializer(self.city_1).data

        response = self.client.get(url)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serialized_data, response.data)

    def test_get_nonexistent(self):
        id = 3
        url = reverse('city-detail', kwargs={'pk': id})

        response = self.client.get(url)

        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)

    def test_get_list(self):
        url = reverse('city-list')
        serialized_data = CitySerializer([self.city_1, self.city_2], many=True).data

        response = self.client.get(url)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serialized_data, response.data)


class LocationApiTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        city = City.objects.create(name='Москва')

        cls.location_1 = Location.objects.create(city=city, street='ул. Тверская', support=1)
        cls.location_2 = Location.objects.create(city=city, street='ул. Тверская', support=2)

    def test_get(self):
        url = reverse('location-detail', kwargs={'pk': self.location_1.id})
        serialized_data = LocationSerializer(self.location_1).data

        response = self.client.get(url)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serialized_data, response.data)

    def test_get_nonexistent(self):
        id = 3
        url = reverse('location-detail', kwargs={'pk': id})

        response = self.client.get(url)

        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)

    def test_get_list(self):
        url = reverse('location-list')
        serialized_data = LocationSerializer([self.location_1, self.location_2], many=True).data

        response = self.client.get(url)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serialized_data, response.data)


class StateApiTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.state_1 = State.objects.create(state=0, logs='Test logs')
        cls.state_2 = State.objects.create(state=1, logs='Test logs')

    def test_get(self):
        url = reverse('state-detail', kwargs={'pk': self.state_1.id})
        serialized_data = StateSerializer(self.state_1).data

        response = self.client.get(url)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serialized_data, response.data)

    def test_get_nonexistent(self):
        id = 3
        url = reverse('state-detail', kwargs={'pk': id})

        response = self.client.get(url)

        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)

    def test_get_list(self):
        url = reverse('state-list')
        serialized_data = StateSerializer([self.state_1, self.state_2], many=True).data

        response = self.client.get(url)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serialized_data, response.data)
