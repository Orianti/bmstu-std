from rest_framework.serializers import ModelSerializer

from .models import *


class CitySerializer(ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class StateSerializer(ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'


class SpecificationsSerializer(ModelSerializer):
    class Meta:
        model = Specifications
        fields = '__all__'


class CameraSerializer(ModelSerializer):
    class Meta:
        model = Camera
        fields = '__all__'


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
