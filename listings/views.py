from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from .forms import SaveData
from .models import HouseListings


# Create your views here.
def index(request):
    listing = HouseListings.objects.order_by('-created_date')[:25]
    paginator = Paginator(listing, 25)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    return render(request, 'index.html', {'items': paged_listings})


def search_lisitng(request):
    listing = HouseListings.objects.order_by('-created_date')
    # keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            listing = listing.filter(description__icontains=keywords)

        # keywords
        if 'city' in request.GET:
            keywords = request.GET['city']
            if keywords != 'c':
                listing = listing.filter(city__iexact=keywords)

        # keywords
        if 'space' in request.GET:
            keywords = request.GET['space']
            if keywords != 'SQ':
                print(keywords)
                listing = listing.filter(city__iexact=keywords)

        # keywords
        if 'price' in request.GET:
            keywords = request.GET['price']
            if keywords:
                listing = listing.filter(price__lte=keywords)
        # keywords
        if 'size' in request.GET:
            keywords = request.GET['size']
            if keywords:
                listing = listing.filter(price__et=keywords)

        if 'furniture' in request.GET:
            keywords = request.GET['furniture']
            if keywords != 'FQ':
                listing = listing.filter(price__iexact=keywords)
    paginator = Paginator(listing, 25)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    return render(request, 'listings.html', {'items': paged_listings, 'num': 100000000})


def listing(request, request_id):
    listin = get_object_or_404(HouseListings, pk=request_id)
    abc = [listin.image1, listin.image2, listin.image3, listin.image4, listin.image5, listin.image6, listin.image7,
           listin.image8, listin.image9, listin.image10, listin.image11, listin.image12]
    count = 0
    img = []
    for i in abc:
        if i:
            img.append(i.url)

    return render(request, 'single_listing.html', {'listing': listin, 'image': img})


def add_item(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SaveData(request.POST, request.FILES or None)
            if form.is_valid():
                custom_object = form.save(commit=False)

                custom_object.user = request.user

                custom_object.save()
                return redirect('listings')
            else:
                return redirect('addListing')
        else:
            form = SaveData()
            return render(request, 'add_listing.html', {'form': form})
    else:
        messages.info(request, "You need to login First")
        return redirect('login_post_ad')
