import os
from http import HTTPStatus

from django.test import TestCase

from app.models import City, Location


class AppTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.passed = 0

    def test_e2e(self):
        self.n = int(os.getenv('REPEATS', 100))
        self.passed = 0

        for i in range(self.n):
            self.__test_e2e()

        self.assertEqual(self.n, self.passed)

    def __test_e2e(self):

        # Add city

        city_data = {
            'name': 'Москва'
        }
        response = self.client.post('/api/v1/city/', data=city_data, content_type='application/json')
        try:
            city = City.objects.all().first()
        except City.DoesNotExist:
            city = {'name': None}

        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        self.assertEqual(city.name, city_data['name'])

        # Add location

        location_data = {
            'city': city.id,
            'street': 'ул. Тверская',
            'support': 1
        }
        response = self.client.post('/api/v1/location/', data=location_data, content_type='application/json')
        try:
            location = Location.objects.all().first()
        except Location.DoesNotExist:
            location = {'street': None}

        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        self.assertEqual(location.street, location_data['street'])
        self.assertEqual(location.city.name, city_data['name'])

        # Update location

        location_new_data = {
            'city': city.id,
            'street': 'ул. Пушкинская',
            'support': 2,
        }

        response = self.client.put(f'/api/v1/location/{location.id}/', data=location_new_data,
                                   content_type='application/json')
        try:
            location = Location.objects.all().first()
        except Location.DoesNotExist:
            location = {'street': None}

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(location.street, location_new_data['street'])
        self.assertEqual(location.city.name, city_data['name'])

        # Delete city

        response = self.client.delete(f'/api/v1/city/{city.id}/')
        exception = False
        try:
            Location.objects.get(id=location.id)
        except Location.DoesNotExist:
            exception = True

        self.assertEqual(response.status_code, HTTPStatus.NO_CONTENT)
        self.assertTrue(exception)

        self.passed += 1
