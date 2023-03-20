import csv
import os
from pathlib import Path
from django.db import models
from django.core.management.base import BaseCommand, CommandError

from temperature_data.models import Country_data, City_data, State_data

#We use the command tools so that we gain access to our models and database connections
#https://docs.djangoproject.com/en/3.1/howto/custom-management-commands/ 


class Command(BaseCommand):
    help = 'Load data from csv'
    def handle(self, *args, **options):
        # drop the data from the table so that if we rerun the file, we don't repeat values
        Country_data.objects.all().delete()
        print("table dropped successfully")
        # create table again
        # open the file to read it into th database
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        with open(str(base_dir) + '/Climate_change_Data/GlobalLandTemperaturesByCountry.csv', newline='') as f:
            reader = csv.reader(f, delimiter=",")
            next(reader) # skip the header line
            for row in reader:
                print(row)
                country = Country_data.objects.create(
                date = row[0],
                average_temperature = row[1],
                average_temperature_uncertainty = row[2],
                country = row[3]
                )
                country.save()

        print("data parsed successfully")

        
