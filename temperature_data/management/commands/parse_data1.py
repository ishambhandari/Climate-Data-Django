import csv
import os
from pathlib import Path
from django.db import models
from django.core.management.base import BaseCommand, CommandError

from temperature_data.models import Country_data, City_data, State_data,Country, City, State


class Command(BaseCommand):
    help = 'Load data from csv'
    def handle(self, *args, **options):
        # drop the data from the table so that if we rerun the file, we don't repeat values
        Country_data.objects.all().delete()
        City_data.objects.all().delete()
        State_data.objects.all().delete()
        Country.objects.all().delete()
        City.objects.all().delete()
        State.objects.all().delete()
        print("table dropped successfully")
        # create table again
        # open the file to read it into th database
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        with open(str(base_dir) + '/Climate_change_Data/GlobalLandTemperaturesByCountry.csv', newline='') as f, open(str(base_dir) + '/Climate_change_Data/GlobalLandTemperaturesByMajorCity.csv', newline='') as C, open(str(base_dir) + '/Climate_change_Data/GlobalLandTemperaturesByState.csv', newline='') as S:
    # code block here
            reader_country = csv.reader(f, delimiter=",")
            next(reader_country) # skip the header line
            unique_countries  = set()
            for row in reader_country:
                unique_countries.add(row[3])

            for u_country  in unique_countries:
                print('here')
                country = Country.objects.create(
                        country = u_country 
                        )
            f.seek(0)
            next(reader_country)
            for u_row in reader_country:
                cid = Country.objects.get(country = u_row[3])
                print('cid', cid.country_id)
                country_data = Country_data.objects.create(
                date = u_row[0],
                average_temperature = u_row[1],
                average_temperature_uncertainty = u_row[2],
                country_id = cid
                )
                country_data.save()

            reader_city= csv.reader(C, delimiter=",")
            next(reader_city) # skip the header line
            unique_city= set()
            for row in reader_city:
                city_instance = Country.objects.get(country = row[4])
                unique_city.add((row[3], city_instance))

            for u_city in unique_city:
                city = City.objects.create(
                        city = u_city[0],
                        country_id = u_city[1]
                        )
            f.seek(0)
            next(reader_city)
            for u_row in reader_city:
                cid = City.objects.get(city = u_row[3])

                country_instance = Country.objects.get(country_id = cid.country_id.country_id)
                print('this is country_ins', country_instance)
                print('cid', cid.city_id)
                city_data= City_data.objects.create(
                date = u_row[0],
                average_temperature = u_row[1],
                average_temperature_uncertainty = u_row[2],
                city_id = cid,
                country_id = country_instance,
                latitude = u_row[5],
                longitude = u_row[6]
                )
                city_data.save()



            reader_state= csv.reader(S, delimiter=",")
            next(reader_state) # skip the header line
            unique_state= set()
            for row in reader_state:
                state_instance= Country.objects.get(country = row[4])
                unique_state.add((row[3], state_instance))

            for u_state in unique_state:
                state = State.objects.create(
                        state = u_state[0],
                        country_id = u_state[1]
                        )
            f.seek(0)
            next(reader_state)
            for u_row in reader_state:
                cid = State.objects.get(state = u_row[3])
                country_instance = Country.objects.get(country_id = cid.country_id.country_id)
                print('cid', cid.state_id)
                state_data= State_data.objects.create(
                date = u_row[0],
                average_temperature = u_row[1],
                average_temperature_uncertainty = u_row[2],
                state_id = cid,
                country_id = country_instance,
                )
                state_data.save()

