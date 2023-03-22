from django.db import models

# Create your models here.
class Country_data(models.Model):
    date = models.DateField()
    average_temperature = models.FloatField()
    average_temperature_uncertainty = models.FloatField()
    country = models.CharField(max_length = 100)

    def __str__(self):
        return f'{self.date},{self.average_temperature},{self.average_temperature_uncertainty},{self.country}'

class Major_city_data(models.Model):
    date = models.DateField()
    average_temperature = models.FloatField()
    average_temperature_uncertainty = models.FloatField()
    major_city = models.CharField(max_length = 100)
    latitude = models.CharField(max_length = 100)
    longitude = models.CharField(max_length = 100)

    def __str__(self):
        return f'{self.date},{self.average_temperature},{self.average_temperature_uncertainty},{self.major_city},{self.latitude},{self.longitude}'


class State_data(models.Model):
    date = models.DateField()
    average_temperature = models.FloatField()
    average_temperature_uncertainty = models.FloatField()
    state = models.CharField(max_length = 100)
    country = models.CharField(max_length = 100)

    def __str__(self):
        return f"{self.date}, {self.state}, {self.country}, {self.average_temperature}"

class Countries(models.Model):
    id = models.AutoField(primary_key = True)
    country = models.CharField(max_length = 100)

    def __str__(self):
        return f'{self.id},{self.country}'

class Major_cities(models.Model):
    id = models.AutoField(primary_key = True)
    major_city = models.CharField(max_length = 100)
    country_id = models.IntegerField()

    def __str__(self):
        return f'{self.id},{self.major_city},{self.country_id}'

class States(models.Model):
    id = models.AutoField(primary_key = True)
    state = models.CharField(max_length = 100)
    country_id = models.IntegerField()

    def __str__(self):
        return f'{self.id},{self.state},{self.country_id}'

    



