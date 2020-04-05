from django.http import HttpResponse
from django.shortcuts import render
from .models import HouseListings
from .forms import SaveData


# Create your views here.
def index(request):
    listing = HouseListings.objects.all()
    return render(request, 'index.html', {'items': listing})


def add_item(request):
    form=SaveData(request.POST)
    if form.is_valid():
        form.save()
    return render(request,'add_listing.html',{'form':form})