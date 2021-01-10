from http import HTTPStatus
from django.test import TestCase

from app.models import City, Location
from app.tests.integration.city_stub import CityStub


class CityTestCase(TestCase):
    def test_add_city(self):
        data = {
            'name': 'Краснодар'
        }

        response = self.client.post('/api/v1/city/', data=data, content_type='application/json')
        try:
            created_city = City.objects.get(name=data['name'])
            is_city_created = True
        except City.DoesNotExist:
            created_city = {'name': None}
            is_city_created = False

        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        self.assertTrue(is_city_created)
        self.assertEqual(created_city.name, data['name'])

    def test_update_city(self):
        city = City.objects.create(name='Москва')

        data = {
            'name': 'Краснодар'
        }

        response = self.client.put(f'/api/v1/city/{city.id}/', data=data, content_type='application/json')
        try:
            updated_city = City.objects.get(name=data['name'])
            is_city_updated = True
        except City.DoesNotExist:
            updated_city = {'name': None}
            is_city_updated = False

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTrue(is_city_updated)
        self.assertEqual(updated_city.name, data['name'])


class LocationTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.city_name = 'Москва'
        city_stub = CityStub(name=cls.city_name)
        cls.city = City.objects.create(name=city_stub.name)

    def test_add_location(self):
        data = {
            'city': self.city.id,
            'street': 'ул. Тверская',
            'support': 1,
        }

        response = self.client.post('/api/v1/location/', data=data, content_type='application/json')
        try:
            created_location = Location.objects.get(street=data['street'])
            is_location_created = True
        except City.DoesNotExist:
            created_location = {'street': None}
            is_location_created = False

        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        self.assertTrue(is_location_created)
        self.assertEqual(created_location.street, data['street'])
        self.assertEqual(created_location.city.name, self.city_name)

    def test_update_location(self):
        location = Location.objects.create(city=self.city, street='ул. Тверская', support=1)

        data = {
            'city': self.city.id,
            'street': 'ул. Пушкинская',
            'support': 2,
        }

        response = self.client.put(f'/api/v1/location/{location.id}/', data=data, content_type='application/json')
        try:
            updated_location = Location.objects.get(street=data['street'])
            is_location_update = True
        except City.DoesNotExist:
            updated_location = {'street': None}
            is_location_update = False

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTrue(is_location_update)
        self.assertEqual(updated_location.street, data['street'])
        self.assertEqual(updated_location.city.name, self.city_name)
