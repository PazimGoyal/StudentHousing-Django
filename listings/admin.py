from django.contrib import admin
from .models import HouseListings



class listings(admin.ModelAdmin):
    list_display = ('title','is_published','price','city')

admin.site.register(HouseListings,listings)

