from django.db import models

# Create your models here.
class Country_data(models.Model):
    date = models.DateField()
    average_temperature = models.CharField(max_length = 10)
    average_temperature_uncertainty = models.CharField(max_length = 10)
    country = models.CharField(max_length = 100)

    def __str__(self):
        return f"{self.date} {self.country}, {self.average_temperature}"

class City_data(models.Model):
    date = models.DateField()
    average_temperature = models.CharField(max_length = 10)
    average_temperature_uncertainty = models.CharField(max_length = 10)
    country = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    latitude = models.CharField(max_length = 100)
    longitude = models.CharField(max_length = 100)

    def __str__(self):
        return f"{self.date}, {self.city}, {self.country}, {self.average_temperature}"

class State_data(models.Model):
    date = models.DateField()
    average_temperature = models.FloatField()
    average_temperature_uncertainty = models.FloatField()
    state = models.CharField(max_length = 100)
    country = models.CharField(max_length = 100)

    def __str__(self):
        return f"{self.date}, {self.state}, {self.country}, {self.average_temperature}"
    



