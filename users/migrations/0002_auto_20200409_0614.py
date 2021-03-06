# Generated by Django 3.0.5 on 2020-04-09 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='city',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='mobile',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='photo',
            field=models.ImageField(blank=True, upload_to='user/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='zipcode',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
