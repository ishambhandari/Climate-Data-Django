from django.db import models

# Create your models here.
class Country(models.Model):
    country_id = models.AutoField(primary_key = True)
    country = models.CharField(max_length = 100)

    def __str__(self):
        return f'{self.id},{self.country}'

class City(models.Model):
    city_id = models.AutoField(primary_key = True)
    city = models.CharField(max_length = 100)
    country_id = models.ForeignKey(Country, on_delete = models.CASCADE, default = 1)

    def __str__(self):
        return f'{self.id},{self.major_city},{self.country_id}'

class State(models.Model):
    state_id = models.AutoField(primary_key = True)
    state = models.CharField(max_length = 100)
    country_id = models.ForeignKey(Country, on_delete = models.CASCADE, default = 1)


class Country_data(models.Model):
    date = models.DateField()
    average_temperature = models.FloatField()
    average_temperature_uncertainty = models.FloatField()
    country_id = models.ForeignKey(Country, on_delete = models.CASCADE, default = 1)

    def __str__(self):
        return f'{self.date},{self.average_temperature},{self.average_temperature_uncertainty},{self.country}'

class City_data(models.Model):
    date = models.DateField()
    average_temperature = models.FloatField()
    average_temperature_uncertainty = models.FloatField()
    city_id = models.ForeignKey(City, on_delete = models.CASCADE, default = 1)
    country_id = models.ForeignKey(Country, on_delete = models.CASCADE, default = 1)
    latitude = models.CharField(max_length = 100)
    longitude = models.CharField(max_length = 100)

    def __str__(self):
        return f'{self.date},{self.average_temperature},{self.average_temperature_uncertainty},{self.major_city},{self.latitude},{self.longitude}'


class State_data(models.Model):
    date = models.DateField()
    average_temperature = models.FloatField()
    average_temperature_uncertainty = models.FloatField()
    state_id = models.ForeignKey(State, on_delete = models.CASCADE, default = 1)
    country_id = models.ForeignKey(Country, on_delete = models.CASCADE, default = 1)

    def __str__(self):
        return f"{self.date}, {self.state}, {self.country}, {self.average_temperature}"

    



