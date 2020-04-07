from django.db import models


# Create your models here.
class UserModel(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    user_name = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    mobile = models.IntegerField()
    password = models.CharField(max_length=10)
    city = models.CharField(max_length=10)
    pin = models.CharField(max_length=7)
    photo = models.ImageField(upload_to='user/%Y/%m/%d')
