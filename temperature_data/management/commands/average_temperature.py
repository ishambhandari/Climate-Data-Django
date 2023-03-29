import os
from pathlib import Path
from django.db import models
from django.core.management.base import BaseCommand, CommandError

from temperature_data.models import Country_data, City_data, State_data,Country, City, State, Country_average, City_average, State_average


class Command(BaseCommand):
    help = 'Getting the average and updating the database'
    def handle(self, *args, **options):
        all_countries = Country.objects.all()
        print(len(all_countries))
        all_cities= City.objects.all()
        all_states = State.objects.all()
        Country_average.objects.all().delete()
        City_average.objects.all().delete()
        State_average.objects.all().delete()
        for country in all_countries:
            print('this is country', country) specific_data = Country_data.objects.filter(country_id = country)  
            average_temp = []
            average_temp_uncertainty = []
            for data in specific_data:
                if data.average_temperature and data.average_temperature_uncertainty:
                    average_temp.append(float(data.average_temperature))
                    average_temp_uncertainty.append(float(data.average_temperature_uncertainty))
            if len(average_temp) != 0 and len(average_temp_uncertainty) != 0:
                    Country_average.objects.create(
                            country = data.country_id,
                            average_temperature = sum(average_temp)/len(average_temp),
                            average_temperature_uncertainty = sum(average_temp_uncertainty)/len(average_temp_uncertainty))
                    average_temp = []
                    average_temp_uncertainty = []

        for city in all_cities:
            print('this is city',city)
            specific_data = City_data.objects.filter(city_id = city)  
            average_temp = []
            average_temp_uncertainty = []
            for data in specific_data:
                print(data.average_temperature)
                if data.average_temperature and data.average_temperature_uncertainty:
                    average_temp.append(float(data.average_temperature))
                    average_temp_uncertainty.append(float(data.average_temperature_uncertainty))
            if len(average_temp) != 0 and len(average_temp_uncertainty) != 0:
                City_average.objects.create(
                            city = data.city_id,
                            average_temperature = sum(average_temp)/len(average_temp),
                            average_temperature_uncertainty = sum(average_temp_uncertainty)/len(average_temp_uncertainty),
                            latitude = specific_data[0].latitude,
                            longitude = specific_data[0].longitude,
                            )

                average_temp = []
                average_temp_uncertainty = []
                

        for state in all_states:
            print('thi is state', state)
            specific_data = State_data.objects.filter(state_id = state)  
            average_temp = []
            average_temp_uncertainty = []
            for data in specific_data:
                if data.average_temperature and data.average_temperature_uncertainty:
                    average_temp.append(float(data.average_temperature))
                    average_temp_uncertainty.append(float(data.average_temperature_uncertainty))
                    
            if len(average_temp) != 0 and len(average_temp_uncertainty) != 0:
                State_average.objects.create(
                            state = data.state_id,
                            average_temperature = sum(average_temp)/len(average_temp),
                            average_temperature_uncertainty = sum(average_temp_uncertainty)/len(average_temp_uncertainty))
                average_temp = []
                average_temp_uncertainty = []








