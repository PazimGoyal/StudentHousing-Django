from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from StudentHomes.settings import MEDIA_ROOT
from .models import HouseListings
from .forms import SaveData
from users.models import UserModel


# Create your views here.
def index(request):
    listing = HouseListings.objects.all()
    paginator = Paginator(listing, 25)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    return render(request, 'index.html', {'items': paged_listings})


def listing(request, request_id):
    listin = get_object_or_404(HouseListings, pk=request_id)
    return render(request, 'listing.html', {'lisitng':listin})


def add_item(request):
    form = SaveData(request.POST, request.FILES or None)
    if form.is_valid():
        form.save()
    return render(request, 'add_listing.html', {'form': form})
