from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField(blank=True)
    city = models.CharField(max_length=10,blank=True)
    zipcode = models.CharField(max_length=10,blank=True)
    photo = models.ImageField(upload_to='user/%Y/%m/%d',blank=True)
