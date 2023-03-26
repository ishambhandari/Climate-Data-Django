# Generated by Django 4.1.7 on 2023-03-26 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('temperature_data', '0008_alter_city_average_average_temperature_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city_average',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='temperature_data.city'),
        ),
        migrations.AlterField(
            model_name='state_average',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='temperature_data.state'),
        ),
    ]