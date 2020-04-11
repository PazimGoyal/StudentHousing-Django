# Generated by Django 3.0.5 on 2020-04-10 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_auto_20200409_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='houselistings',
            name='building_type',
            field=models.CharField(choices=[('NOT AVAILABLE', 'NOT AVAILABLE'), ('Apartment Building', 'Apartment Building'), ('House', 'House'), ('Basement', 'Basement')], max_length=18),
        ),
        migrations.AlterField(
            model_name='houselistings',
            name='furnished',
            field=models.TextField(choices=[('NOT AVAILABLE', 'NOT AVAILABLE'), ('Not Furnished', 'NOT FURNISHED'), ('Fully Furnished', 'FULLY FURNISHED'), ('Semi Furnished', 'SEMI-FURNISHED')]),
        ),
        migrations.AlterField(
            model_name='houselistings',
            name='space_given',
            field=models.CharField(choices=[('NOT AVAILABLE', 'NOT AVAILABLE'), ('Shared Bedroom', 'Shared Bedroom'), ('Private Bedroom', 'Private Bedroom'), ('Entire Place', 'Entire Apartment/House')], max_length=15),
        ),
    ]
