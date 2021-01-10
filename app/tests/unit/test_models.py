from unittest.mock import MagicMock

from django.test import TestCase

from app.models import City, Location, State
from app.tests.unit.location_builder import LocationBuilder
from app.tests.unit.state_stub import StateStub


class CityTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.city_1 = City.objects.create(name='Москва')
        cls.city_2 = City.objects.create(name='Санкт-Петербург')

    def test_get_by_id(self):
        city_1 = City.objects.get(id=self.city_1.id)
        city_2 = City.objects.get(id=self.city_2.id)

        self.assertEqual((self.city_1, self.city_2), (city_1, city_2))

    def test_get_nonexistent_by_id(self):
        id = 9
        exception = False

        try:
            City.objects.get(id=id)
        except City.DoesNotExist:
            exception = True

        self.assertTrue(exception)

    def test_update_name(self):
        name = 'Казань'
        self.city_1.save = MagicMock()

        self.city_1.update_name(name)

        self.assertEqual(name, self.city_1.name)
        self.city_1.save.assert_called_once()


class LocationTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.location_1 = LocationBuilder(city_name='Москва') \
            .with_street('ул. Тверская') \
            .with_support(1) \
            .build()
        cls.location_2 = LocationBuilder(city_name='Санкт-Петербург') \
            .with_street('Невский проспект') \
            .with_support(2) \
            .build()

    def test_get_by_id(self):
        location_1 = Location.objects.get(id=self.location_1.id)
        location_2 = Location.objects.get(id=self.location_2.id)

        self.assertEqual((self.location_1, self.location_2), (location_1, location_2))

    def test_get_nonexistent_by_id(self):
        id = 21
        exception = False

        try:
            Location.objects.get(id=id)
        except Location.DoesNotExist:
            exception = True

        self.assertTrue(exception)

    def test_update_name(self):
        portable = 0
        self.location_1.save = MagicMock()

        self.location_1.make_portable()

        self.assertEqual(portable, self.location_1.support)
        self.location_1.save.assert_called_once()


class StateTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        state_stub_1 = StateStub(state=0, logs='Test log')
        state_stub_2 = StateStub(state=1, logs='Test log')

        cls.state_1 = State.objects.create(state=state_stub_1.state, logs=state_stub_1.logs)
        cls.state_2 = State.objects.create(state=state_stub_2.state, logs=state_stub_2.logs)

    def test_get_by_id(self):
        state_1 = State.objects.get(id=self.state_1.id)
        state_2 = State.objects.get(id=self.state_2.id)

        self.assertEqual((self.state_1, self.state_2), (state_1, state_2))

    def test_get_nonexistent_by_id(self):
        id = 9
        exception = False

        try:
            State.objects.get(id=id)
        except State.DoesNotExist:
            exception = True

        self.assertTrue(exception)

    def test_update_name(self):
        logs = 'Test updated logs'
        self.state_1.save = MagicMock()

        self.state_1.update_logs(logs)

        self.assertEqual(logs, self.state_1.logs)
        self.state_1.save.assert_called_once()
