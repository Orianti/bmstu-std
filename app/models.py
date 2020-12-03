from django.db import models


class City(models.Model):
    name = models.CharField(max_length=30, verbose_name='название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'город'
        verbose_name_plural = 'города'


class Location(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='город')
    street = models.CharField(max_length=100, verbose_name='улица')
    support = models.IntegerField(verbose_name='номер опоры')
    notes = models.TextField(verbose_name='заметки', default='', blank=True)

    def get_location(self):
        if self.support:
            return f'{self.city}, {self.street} (опора {self.support})'
        else:
            return f'{self.city}, {self.street}'

    def __str__(self):
        return self.get_location()

    class Meta:
        verbose_name = 'положение'
        verbose_name_plural = 'положения'


class State(models.Model):
    STATES = (
        (0, 'OK'),
        (1, 'WARNING'),
        (2, 'ERROR'),
        (3, 'FAILURE'),
    )

    state = models.IntegerField(choices=STATES, verbose_name='состояние')
    logs = models.TextField(verbose_name='журнал', default='', blank=True)

    def get_state(self):
        return f'{self.get_state_display()}'

    def __str__(self):
        return f'{self.get_state()} ({self.logs})'

    class Meta:
        verbose_name = 'состояние'
        verbose_name_plural = 'состояния'


class Specifications(models.Model):
    TYPES = (
        (0, 'SPEED'),
        (1, 'AVERAGE SPEED'),
        (2, 'RED LIGHT'),
        (3, 'DOUBLE WHITE LINE'),
        (4, 'BUS LANE'),
        (5, 'TOLLBOOTH'),
        (6, 'LEVEL CROSSING'),
        (7, 'CONGESTION CHARGE'),
    )

    type = models.IntegerField(choices=TYPES, verbose_name='тип')
    producer = models.CharField(max_length=100, verbose_name='производитель')
    date_of_manufacture = models.DateField(verbose_name='дата производства')
    service_frequency = models.IntegerField(verbose_name='частота сервисного обслуживания')
    notes = models.TextField(verbose_name='заметки', default='', blank=True)

    def get_type(self):
        return self.get_type_display()

    def __str__(self):
        try:
            return f'{self.get_type()} ({self.camera.__str__()})'
        except Camera.DoesNotExist:
            return f'{self.get_type()}'

    class Meta:
        verbose_name = 'спецификация'
        verbose_name_plural = 'спецификации'


class Camera(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, verbose_name='местоположение')
    specifications = models.OneToOneField(Specifications, on_delete=models.CASCADE, verbose_name='спецификации')
    state = models.ForeignKey(State, on_delete=models.CASCADE, verbose_name='состояние')

    def __str__(self):
        return f'Камера №{self.id}'

    class Meta:
        verbose_name = 'камера'
        verbose_name_plural = 'камеры'


class Service(models.Model):
    camera = models.ForeignKey(Camera, on_delete=models.CASCADE, verbose_name='ID камеры')
    service_organization = models.CharField(max_length=100, verbose_name='сервисная организация')

    registration_date = models.DateField(auto_now_add=True)
    service_data = models.DateField(verbose_name='дата сервиса')
    info = models.TextField(verbose_name='информация', default='', blank=True)

    def __str__(self):
        return f'сервис №{self.id}'

    class Meta:
        verbose_name = 'сервис'
        verbose_name_plural = 'сервисы'
