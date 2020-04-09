from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

space = (
    ('SR', 'Shared Room'), ('PB', 'Private bedroom'), ('EP', 'Entire Apartment/House'))
typeB = (('AB', 'Apartment Building'), ('H', 'House'), ('B', 'Basement'))
city = (('MTL', 'Montreal'), ('TOR', 'Toronto'))
furnish = (('NF', 'NOT FURNISHED'), ('FF', 'FULLY FURNISHED'), ('SF', 'SEMI-FURNISHED'))


class HouseListings(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    address = models.CharField(max_length=200, default="")
    city = models.CharField(max_length=3, choices=city)
    state = models.CharField(max_length=50)
    zipCode = models.CharField(max_length=10)
    building_type = models.CharField(choices=typeB, max_length=2)
    garage = models.BooleanField(default=False)
    space_given = models.CharField(choices=space, max_length=2)
    created_date = models.DateTimeField(default=timezone.now, blank=True)
    is_published = models.BooleanField(default=True)
    image1 = models.ImageField(upload_to='photos/%Y%m%d/', default="default.jpeg")
    image2 = models.ImageField(upload_to='photos/%Y%m%d/', blank=True)
    image3 = models.ImageField(upload_to='photos/%Y%mb%d/', blank=True)
    image4 = models.ImageField(upload_to='photos/%Y%m%d/', blank=True)
    image5 = models.ImageField(upload_to='photos/%Y%m%d/', blank=True)
    image6 = models.ImageField(upload_to='photos/%Y%m%d/', blank=True)
    image7 = models.ImageField(upload_to='photos/%Y%m%d/', blank=True)
    image8 = models.ImageField(upload_to='photos/%Y%m%d/', blank=True)
    image9 = models.ImageField(upload_to='photos/%Y%mb%d/', blank=True)
    image10 = models.ImageField(upload_to='photos/%Y%m%d/', blank=True)
    image11 = models.ImageField(upload_to='photos/%Y%m%d/', blank=True)
    image12 = models.ImageField(upload_to='photos/%Y%m%d/', blank=True)
    bathrooms = models.DecimalField(max_digits=2, default=1, decimal_places=1)
    electricityIncluded = models.BooleanField(default=True)
    wifiIncluded = models.BooleanField(default=False)
    animalsAllowed = models.BooleanField(default=True)
    furnished = models.TextField(default="NF", choices=furnish)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
