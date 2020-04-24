import sys
from io import BytesIO

from PIL import Image
from django.contrib.auth.models import User
from django.core.files import File
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from django.utils import timezone

space = (('NOT AVAILABLE', 'NOT AVAILABLE'),
         ('Shared Bedroom', 'Shared Bedroom'), ('Private Bedroom', 'Private Bedroom'),
         ('Entire Place', 'Entire Apartment/House'))
typeB = (('NOT AVAILABLE', 'NOT AVAILABLE'), ('Apartment Building', 'Apartment Building'), ('House', 'House'),
         ('Basement', 'Basement'))
city = (('Montreal', 'Montreal'), ('Toronto', 'Toronto'))
furnish = (('NOT AVAILABLE', 'NOT AVAILABLE'),
           ('Not Furnished', 'NOT FURNISHED'), ('Fully Furnished', 'FULLY FURNISHED'),
           ('Semi Furnished', 'SEMI-FURNISHED'))


def compress(image):
    im = Image.open(image)
    im_io = BytesIO()
    im.save(im_io, 'JPEG', quality=60)
    new_image = File(im_io, name=image.name)
    return new_image


class HouseListings(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    address = models.CharField(max_length=200, default="")
    city = models.CharField(max_length=10, choices=city)
    zipCode = models.CharField(max_length=10)
    building_type = models.CharField(choices=typeB, max_length=18)
    garage = models.BooleanField(default=False)
    space_given = models.CharField(choices=space, max_length=15)
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
    electricityIncluded = models.BooleanField(default=False)
    wifiIncluded = models.BooleanField(default=False)
    animalsAllowed = models.BooleanField(default=False)
    furnished = models.TextField(choices=furnish)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    size = models.DecimalField(blank=True, decimal_places=1, max_digits=2, default=3.5)
    bathrooms = models.DecimalField(blank=True, decimal_places=1, max_digits=2, default=2)

    def save(self, *args, **kwargs):

        if self.image1:
            self.image1 = self.compressImage(self.image1)
        if self.image2:
            self.image2 = self.compressImage(self.image2)
        if self.image3:
            self.image3 = self.compressImage(self.image3)
        if self.image4:
            self.image4 = self.compressImage(self.image4)
        if self.image5:
            self.image5 = self.compressImage(self.image5)
        if self.image6:
            self.image6 = self.compressImage(self.image6)
        if self.image7:
            self.image7 = self.compressImage(self.image7)
        if self.image8:
            self.image8 = self.compressImage(self.image8)
        if self.image9:
            self.image9 = self.compressImage(self.image9)
        if self.image10:
            self.image10 = self.compressImage(self.image10)
        if self.image11:
            self.image11 = self.compressImage(self.image11)
        if self.image12:
            self.image12 = self.compressImage(self.image12)
        super(HouseListings, self).save(*args, **kwargs)
        if self.image1:
            self.thumbImage(self.image1)
        if self.image2:
            self.thumbImage(self.image2)
        if self.image3:
            self.thumbImage(self.image3)
        if self.image4:
            self.thumbImage(self.image4)
        if self.image5:
            self.thumbImage(self.image5)
        if self.image6:
            self.thumbImage(self.image6)
        if self.image7:
            self.thumbImage(self.image7)
        if self.image8:
            self.thumbImage(self.image8)
        if self.image9:
            self.thumbImage(self.image9)
        if self.image10:
            self.thumbImage(self.image10)
        if self.image11:
            self.thumbImage(self.image11)
        if self.image12:
            self.thumbImage(self.image12)


    def compressImage(self, uploadedImage):
        imageTemproary = Image.open(uploadedImage)
        (width, height) = imageTemproary.size
        print("===========================================================================================")
        print(width,height)
        max=700
        ratio=width/height
        size=(width,height)
        if height>max:
            size=(int(max*ratio),max)
        outputIoStream = BytesIO()
        imageTemproaryResized = imageTemproary.resize(size)
        imageTemproaryResized.save(outputIoStream, format='JPEG', quality=60)
        outputIoStream.seek(0)
        uploadedImage = InMemoryUploadedFile(outputIoStream, 'ImageField', str(self.title)+"_"+"%s.jpg" % uploadedImage.name.split('.')[0],
                                                 'image/jpeg', sys.getsizeof(outputIoStream), None)
        print("-------------------------------------------------------------------------------------")
        print(size)

        return uploadedImage

    def thumbImage(self, photo):
        image = Image.open(photo.file)
        resized_image = image.resize((300, 200), Image.ANTIALIAS)
        resized_image.save(photo.file.name.split('.')[0] + "-thumbnail.jpg", quality=60)
