from django.db import models
from django.utils import timezone
from users.models import UserModel

space = (('SHARED ROOM', 'Shared Room'), ('PRIVATE BEDROOM', 'Private bedroom'), ('ENTIRE PLACE', 'Entire Apartment/House'))
typeB = (('APPARTMENT BUILDING', 'Apartment Building'), ('HOUSE', 'House'), ('BASEMENT', 'Basement'))
city = (('MONTREAL', 'Montreal'), ('TORONTO', 'Toronto'))


class HouseListings(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    address = models.CharField(max_length=200,default="")
    city = models.CharField(max_length=50, choices=city)
    state = models.CharField(max_length=50)
    zipCode = models.CharField(max_length=10)
    building_type = models.CharField(choices=typeB,max_length=20)
    garage = models.BooleanField(default=False)
    space_given = models.CharField(choices=space,max_length=20)
    created_date = models.DateTimeField(default=timezone.now, blank=True)
    is_published = models.BooleanField(default=True)
    image1 = models.ImageField(upload_to='photos/%Y%m%d/', default="default.jpeg")
    image2 = models.ImageField(upload_to='photos/%Y%m%d/', blank=True)
    image3 = models.ImageField(upload_to='photos/%Y%mb%d/', blank=True)
    image4 = models.ImageField(upload_to='photos/%Y%m%d/', blank=True)
    image5 = models.ImageField(upload_to='photos/%Y%m%d/', blank=True)
    image6 = models.ImageField(upload_to='photos/%Y%m%d/', blank=True)
#    by = models.ForeignKey(UserModel,on_delete=models.CASCADE,blank=True)
