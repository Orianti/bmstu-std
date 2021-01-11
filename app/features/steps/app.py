from http import HTTPStatus
from behave import *

from app.models import Location

use_step_matcher("re")


@given("city")
def step_impl(context):
    city_data = {
        'name': 'Москва'
    }
    context.response = context.test.client.post('/api/v1/city/', data=city_data, content_type='application/json')


@given("location")
def step_impl(context):
    location_data = {
        'city': 1,
        'street': 'ул. Тверская',
        'support': 1
    }
    context.response = context.test.client.post('/api/v1/location/', data=location_data,
                                                content_type='application/json')


@when('I delete city')
def step_impl(context):
    context.response = context.test.client.delete(f'/api/v1/city/1/')


@then('response status code should be 204')
def step_impl(context):
    context.test.assertEqual(context.response.status_code, HTTPStatus.NO_CONTENT)


@then('I should not see location')
def step_impl(context):
    exception = False
    try:
        Location.objects.get(id=1)
    except Location.DoesNotExist:
        exception = True

    context.test.assertEqual(context.response.status_code, HTTPStatus.NO_CONTENT)
    context.test.assertTrue(exception)
