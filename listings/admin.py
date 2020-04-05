from django.contrib import admin
from .models import HouseListings



class listings(admin.ModelAdmin):
    list_display = ('title','price','location')

admin.site.register(HouseListings,listings)

