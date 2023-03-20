from django.test import TestCase
from temperature_data.models import Country_data, City_data, State_data
class TestModels(TestCase):
    def setUp(self):
        self.country1= Country_data.objects.create(
                date = '2012-02-02',
                average_temperature = 24,
                average_temperature_uncertainty = 34.1,
                country = 'Nepal'
                )
        self.city1 = City_data.objects.create(
                date = '2013-01-23',
                average_temperature = 24,
                average_temperature_uncertainty = 34.1,
                city = 'Kathmandu',
                country = 'Nepal',
                latitude = 33.2,
                longitude = 35.2,
                )
        self.state1 = State_data.objects.create(
                date = '2014-2-1',
                average_temperature = 22,
                average_temperature_uncertainty = 12,
                state = 'Bagmati',
                country = 'Nepal'
                )

    def test_data_exists(self):
        self.assertEqual(self.country1.date, '2012-02-02')
        self.assertEqual(self.city1.latitude, 33.2)
        self.assertEqual(self.state1.average_temperature, 22)

