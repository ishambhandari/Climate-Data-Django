from django.db import models

# Create your models here.
class Country(models.Model):
    country_id = models.AutoField(primary_key = True)
    country = models.CharField(max_length = 100)

    def __str__(self):
        return f'{self.country_id},{self.country}'

class City(models.Model):
    city_id = models.AutoField(primary_key = True)
    city = models.CharField(max_length = 100)
    country_id = models.ForeignKey(Country, on_delete = models.CASCADE, default = 1)

    def __str__(self):
        return f'{self.city_id},{self.country_id},{self.city}'

class State(models.Model):
    state_id = models.AutoField(primary_key = True)
    state = models.CharField(max_length = 100)
    country_id = models.ForeignKey(Country, on_delete = models.CASCADE, default = 1)

    def __str__(self):
        return f'{self.state_id},{self.state},{self.country_id}'


class Country_data(models.Model):
    date = models.DateField()
    average_temperature = models.CharField(max_length = 10)
    average_temperature_uncertainty = models.CharField(max_length = 10)
    country_id = models.ForeignKey(Country, on_delete = models.CASCADE, default = 1)

    def __str__(self):
        return f'{self.date},{self.average_temperature},{self.average_temperature_uncertainty},{self.country_id}'

class City_data(models.Model):
    date = models.DateField()
    average_temperature = models.CharField(max_length = 10)
    average_temperature_uncertainty = models.CharField(max_length = 10)
    city_id = models.ForeignKey(City, on_delete = models.CASCADE, default = 1)
    country_id = models.ForeignKey(Country, on_delete = models.CASCADE, default = 1)
    latitude = models.CharField(max_length = 100)
    longitude = models.CharField(max_length = 100)

    def __str__(self):
        return f'{self.date},{self.average_temperature},{self.average_temperature_uncertainty},{self.city_id},{self.latitude},{self.longitude}'


class State_data(models.Model):
    date = models.DateField()
    average_temperature = models.CharField(max_length = 10)
    average_temperature_uncertainty = models.CharField(max_length = 10)
    state_id = models.ForeignKey(State, on_delete = models.CASCADE, default = 1)
    country_id = models.ForeignKey(Country, on_delete = models.CASCADE, default = 1)

    def __str__(self):
        return f"{self.date}, {self.state}, {self.country}, {self.average_temperature}"

class Country_average(models.Model):
    country = models.ForeignKey(Country, on_delete = models.CASCADE)
    average_temperature = models.FloatField(max_length = 10)
    average_temperature_uncertainty = models.FloatField()

    def __str__(self):
        return f"{self.country.country_id}, {self.country}, {self.average_temperature}"

class City_average(models.Model):
    city= models.ForeignKey(City, on_delete = models.CASCADE)
    average_temperature = models.FloatField()
    average_temperature_uncertainty = models.FloatField()
    latitude = models.CharField(max_length = 10, null = True)
    longitude = models.CharField(max_length = 10, null = True)

    def __str__(self):
        return f"{self.city.city_id},{self.city}, {self.average_temperature}, {self.latitude}, {self.longitude}"

class State_average(models.Model):
    state = models.ForeignKey(State, on_delete = models.CASCADE)
    average_temperature = models.FloatField()
    average_temperature_uncertainty = models.FloatField()
    
    def __str__(self):
        return f"{self.state.state_id},{self.state}, {self.average_temperature}"





