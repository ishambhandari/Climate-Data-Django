# Generated by Django 4.1.7 on 2023-03-19 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('average_temperature', models.FloatField()),
                ('average_temperature_uncertainty', models.FloatField()),
                ('country', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('latitude', models.CharField(max_length=100)),
                ('longitude', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Country_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('average_temperature', models.FloatField()),
                ('average_temperature_uncertainty', models.FloatField()),
                ('country', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='State_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('average_temperature', models.FloatField()),
                ('average_temperature_uncertainty', models.FloatField()),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
    ]
