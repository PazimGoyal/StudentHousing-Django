from decimal import Decimal

from django.contrib import messages
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from listings.choices import space_type_c, city_c, order_c, building_type_c, furnished_c
from .forms import SaveData
from .models import HouseListings
from users.models import LikedListings

# Create your views here.
def index(request):
    listing = HouseListings.objects.order_by('-created_date')[:5]
    return render(request, 'index.html',
                  {'items': listing, 's': space_type_c, 'c': city_c, 'b': building_type_c, 'o': order_c,
                   'f': furnished_c})


def listings(request):
    if 'order' in request.GET:
        listing = HouseListings.objects.order_by(request.GET['order'])
    else:
        listing = HouseListings.objects.order_by('-created_date')

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
    if 'space_given' in request.GET:
        keywords = request.GET['space_given']
        if keywords != 'NOT AVAILABLE':
            listing = listing.filter(space_given__iexact=keywords)

    if 'building_type' in request.GET:
        keywords = request.GET['building_type']
        if keywords != 'NOT AVAILABLE':
            listing = listing.filter(building_type__iexact=keywords)

    # keywords
    if 'min_price' in request.GET:
        keywords = request.GET['min_price']
        if keywords:
            listing = listing.filter(price__gte=keywords)
    if 'max_price' in request.GET:
        keywords = request.GET['max_price']
        if keywords:
            listing = listing.filter(price__lte=keywords)

    # keywords
    if 'size' in request.GET:
        keywords = request.GET['size']
        if keywords:
            listing = listing.filter(size=Decimal(keywords))

    if 'bathroom' in request.GET:
        keywords = request.GET['bathroom']
        if keywords:
            listing = listing.filter(bathrooms=Decimal(keywords))

    if 'furniture' in request.GET:
        keywords = request.GET['furniture']
        if keywords != 'NOT AVAILABLE':
            listing = listing.filter(furnished__iexact=keywords)

    if 'garage' in request.GET:
        listing = listing.filter(garage=1)

    if 'animalsAllowed' in request.GET:
        listing = listing.filter(animalsAllowed=1)
    if 'electricityIncluded' in request.GET:
        listing = listing.filter(electricityIncluded=1)

    if 'wifiIncluded' in request.GET:
        listing = listing.filter(wifiIncluded=1)

    paginator = Paginator(listing, 25)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    return render(request, 'listings.html',
                  {'items': paged_listings, 'vals': request.GET, 's': space_type_c, 'c': city_c, 'b': building_type_c,
                   'o': order_c, 'f': furnished_c})


def single_listing(request, request_id):
    currentuserliked =False
    listin = get_object_or_404(HouseListings, pk=request_id)

    if request.user.is_authenticated:
        liked=LikedListings.objects.filter(user=request.user).filter(advertisement=listin)
        if liked:
            currentuserliked=True

    abc = [listin.image1, listin.image2, listin.image3, listin.image4, listin.image5, listin.image6, listin.image7,
           listin.image8, listin.image9, listin.image10, listin.image11, listin.image12]
    count = 0
    img = []
    for i in abc:
        if i:
            img.append(i.url)
    return render(request, 'single_listing.html', {'listing': listin, 'image': img,'likes':currentuserliked})


def add_item(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SaveData(request.POST, request.FILES or None)
            print(request.POST)
            if form.is_valid():
                custom_object = form.save(commit=False)
                custom_object.user = request.user
                custom_object.save()
                return redirect('listings')
            else:
                messages.error(request, form.errors)
                return redirect('addListing')
        else:
            form = SaveData()
        return render(request, 'add_listing.html',
                      {'form': form, 's': space_type_c, 'c': city_c, 'b': building_type_c, 'o': order_c,
                       'f': furnished_c})
    else:
        messages.info(request, "You need to login First")
        return redirect('login_post_ad')


def mail_sending(request):
    if request.user.is_authenticated:
        if request.POST:
            data = request.POST
            print("--------------------------------------------------------------")
            print(data)
            print("--------------------------------------------------------------")
            description = """This mail is regarding your ad. on studentHousing.com 
view your ad. here :""" + "http://10.0.0.81:8000" + data['listing_url'] + """   
    
""" + "Requested by:- " + request.user.first_name + " " + request.user.last_name + "\n" + data['phone'] + "\n" + data[
'description'] + """
    
You can reply to user using website chatting service or directly reply at """ + request.user.email + """   
Thankyou for using StudentHousing.com"""
            send = send_mail('no-reply - student housing your ad. ', description, data['email'], [data['listing_by'], ])
            if send:
                messages.success(request, "Mail Sent Successfully")
            else:
                messages.error(request, "Fail to send mail")
            new_url = data['listing_url']
        return redirect(new_url)
    else:
        messages.info(request, "You need to Login First")
        return redirect('login')


def edit_listing(request, request_id):
    # ModelClass.objects.filter(name='bar').update(name="foo")

    listing = get_object_or_404(HouseListings, pk=request_id)

    if listing.user == request.user:
        if request.method == 'POST':
            form = SaveData(request.POST, request.FILES, instance=listing)
            if form.is_valid():
                listing.save()
                return redirect('listings')

        else:
            form = SaveData()

        return render(request, 'add_listing.html',
                      {' form': form, 'listing': listing, 's': space_type_c, 'c': city_c, 'b': building_type_c,
                       'o': order_c,
                       'f': furnished_c})
    else:
        messages.error("You Cannot Edit This Listing")
        return redirect('dashboard')


def delete_listing(request,request_id):
    listing = get_object_or_404(HouseListings, pk=request_id)
    if request.user.is_authenticated and (listing.user==request.user):
        listing = get_object_or_404(HouseListings, pk=request_id)
        listing.delete()
        return redirect('dashboard')
    else:
        return HttpResponse("ERROR 505")