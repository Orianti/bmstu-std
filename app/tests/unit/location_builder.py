from app.models import Location, City


class LocationBuilder(object):
    def __init__(self, city_name, street='', support=0):
        city = City.objects.create(name=city_name)
        self.location = Location.objects.create(city=city, street=street, support=support)

    def with_street(self, street):
        self.location.street = street
        return self

    def with_support(self, support):
        self.location.street = support
        return self

    def with_note(self, note):
        self.location.note = note
        return self

    def build(self):
        return self.location
