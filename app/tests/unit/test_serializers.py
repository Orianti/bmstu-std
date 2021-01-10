from unittest.mock import MagicMock

from django.test import TestCase

from app.models import City, Location, State
from app.serializers import CitySerializer, LocationSerializer, StateSerializer


class CitySerializerTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.city_1 = City.objects.create(name='Москва')
        cls.city_2 = City.objects.create(name='Санкт-Петербург')

        cls.city_serializer = CitySerializer(cls.city_1, context={'request': MagicMock()})

    def test_content(self):
        expected_data = [
            {
                'id': self.city_1.id,
                'name': self.city_1.name
            },
            {
                'id': self.city_2.id,
                'name': self.city_2.name
            }
        ]

        data = CitySerializer([self.city_1, self.city_2], many=True).data

        self.assertEqual(expected_data, data)

    def test_create_name(self):
        data = {
            'name': 'Казань'
        }
        exception = False

        try:
            self.city_serializer.create(data)
        except TypeError:
            exception = True

        self.assertFalse(exception)

    def test_update_name(self):
        new_name = 'Казань'

        self.city_serializer.update(self.city_1, {'name': new_name})

        self.assertEqual(new_name, self.city_1.name)


class LocationSerializerTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.city = City.objects.create(name='Москва')

        cls.location_1 = Location.objects.create(city=cls.city, street='ул. Тверская', support=1)
        cls.location_2 = Location.objects.create(city=cls.city, street='ул. Тверская', support=2)

        cls.location_serializer = LocationSerializer(cls.location_1, context={'request': MagicMock()})

    def test_content(self):
        expected_data = [
            {
                'id': self.location_1.id,
                'street': self.location_1.street,
                'support': self.location_1.support,
                'notes': self.location_1.notes,
                'city': self.location_1.city.id
            },
            {
                'id': self.location_2.id,
                'street': self.location_2.street,
                'support': self.location_2.support,
                'notes': self.location_2.notes,
                'city': self.location_2.city.id
            }
        ]

        data = LocationSerializer([self.location_1, self.location_2], many=True).data

        self.assertEqual(expected_data, data)

    def test_create_name(self):
        data = {
            'street': 'ул. Тверская',
            'support': 3,
            'notes': '',
            'city': self.city
        }
        exception = False

        try:
            self.location_serializer.create(data)
        except TypeError:
            exception = True

        self.assertFalse(exception)

    def test_update_name(self):
        data = {
            'street': 'ул. Бауманская',
            'support': 10,
            'notes': '',
            'city': self.city
        }

        self.location_serializer.update(self.location_1, data)

        self.assertEqual(data, {
            'street': self.location_1.street,
            'support': self.location_1.support,
            'notes': self.location_1.notes,
            'city': self.location_1.city,
        })


class StateSerializerTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.state_1 = State.objects.create(state=0, logs='Test logs')
        cls.state_2 = State.objects.create(state=1, logs='Test logs')

        cls.state_serializer = StateSerializer(cls.state_1, context={'request': MagicMock()})

    def test_content(self):
        expected_data = [
            {
                'id': self.state_1.id,
                'state': self.state_1.state,
                'logs': self.state_1.logs
            },
            {
                'id': self.state_2.id,
                'state': self.state_2.state,
                'logs': self.state_2.logs
            }
        ]

        data = StateSerializer([self.state_1, self.state_2], many=True).data

        self.assertEqual(expected_data, data)

    def test_create_name(self):
        data = {
            'state': 0,
            'logs': 'Test logs'
        }
        exception = False

        try:
            self.state_serializer.create(data)
        except TypeError:
            exception = True

        self.assertFalse(exception)

    def test_update_name(self):
        data = {
            'state': 2,
            'logs': 'New logs'
        }

        self.state_serializer.update(self.state_1, data)

        self.assertEqual(data, {
            'state': self.state_1.state,
            'logs': self.state_1.logs
        })
