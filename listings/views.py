
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from .forms import SaveData
from .models import HouseListings


# Create your views here.
def index(request):
    listing = HouseListings.objects.order_by('-created_date')[:5]
    return render(request, 'index.html', {'items': listing})


def listings(request):
    listing = HouseListings.objects.order_by('-created_date')


    if 'order' in request.GET:
        listing = HouseListings.objects.order_by(request.GET['order'])


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
                listing = listing.filter(size__iexact=keywords)

        # keywords
        if 'min-price' in request.GET:
            keywords = request.GET['min-price']
            if keywords:
                listing = listing.filter(price__gte=keywords)
        if 'max-price' in request.GET:
            keywords = request.GET['max-price']
            if keywords:
                listing = listing.filter(price__lte=keywords)

        # keywords
        if 'size' in request.GET:
            keywords = request.GET['size']
            if keywords:
                listing = listing.filter(size__et=keywords)

        if 'furniture' in request.GET:
            keywords = request.GET['furniture']
            if keywords != 'FQ':
                listing = listing.filter(furnished__iexact=keywords)
    paginator = Paginator(listing, 15)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    return render(request, 'listings.html', {'items': paged_listings,'vals':request.GET})


def single_listing(request, request_id):
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
        return render(request, 'add_listing.html', {'form': form})
    else:
        messages.info(request, "You need to login First")
        return redirect('login_post_ad')


def mail_sending(request):
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
