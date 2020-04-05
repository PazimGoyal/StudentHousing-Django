
from django.db import models
from django.utils import timezone


class HouseListings(models.Model):
    title=models.CharField(max_length=500)
    discription=models.CharField(max_length=20000)
    price=models.FloatField(max_length=10)
    location=models.CharField(max_length=500)
    type=models.CharField(max_length=10)
    image=models.CharField(max_length=2085,default="../images/default.jpeg")
    extra1 = models.CharField(max_length=50)
    extra2 = models.CharField(max_length=30)
    extra3 = models.CharField(max_length=20)
    extra4 = models.CharField(max_length=10)
    #created_date = models.DateTimeField('date created', default=timezone.now)

