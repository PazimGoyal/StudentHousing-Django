from django.contrib import messages, auth
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from listings.models import HouseListings
from .forms import myForm
from .models import UserModel,LikedListings


# Create your views here.
def login(request):
    if request.method == 'POST':
        form = User(request.POST, request.FILES)
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are logged In")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid Username or Password")
            return redirect('login')
    else:
        return render(request, 'login.html', {})


def login_post_ad(request):
    if request.method == 'POST':
        form = User(request.POST, request.FILES)
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are logged In")
            return redirect('addListing')
        else:
            messages.error(request, "Invalid Username or Password")
            return redirect('login')
    else:
        return render(request, 'login.html', {})


def logout_view(request):
    logout(request)
    return redirect('listings')


def dashboard(request):
    if request.user.is_authenticated:
        myobject = HouseListings.objects.order_by('-created_date').filter(user=request.user)
        myobject2 = get_object_or_404(UserModel,user=request.user)
        return render(request, 'dashboard.html', {'items': myobject, 'userinfo': myobject2})
    else:
        messages.info(request, "You need to Login First")
        return redirect('login')


def register(request):
    if request.method == 'POST':
        form = User(request.POST)
        form2 = myForm(request.POST, request.FILES)
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        phone = request.POST['phone']
        password = request.POST['password']
        rpassword = request.POST['rpassword']

        if password == rpassword:
            if User.objects.filter(username=username).exists():
                messages.error(request, "User Already Exist with thaat user name")
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email  already Exists ")
                else:
                    user = User.objects.create_user(username=username, email=email, password=password,
                                                    first_name=first_name, last_name=last_name)
                    user.save()
                    if form2.is_valid():
                        object_my = form2.save(commit=False)
                        object_my.user = user
                        object_my.save()
                    return redirect("login")
        else:
            messages.error(request, "Passwords Do Not Match")
    else:
        form = User()
        form2 = myForm()
    return render(request, 'register.html', {'form': form, 'form2': form2})

def likes(request):
    id=int(request.GET['listing'])
    print(1)
    listing = get_object_or_404(HouseListings, pk=id)
    print(2)
    obj=LikedListings.objects.filter(user=request.user,advertisement=listing)
    print(3)
    print(obj)
    print(4)
    if obj:
        obj.delete()
        print("DELETED")
    else:
        print("CREATED")
        record=LikedListings(user=request.user,advertisement=listing)
        record.save()
    return HttpResponse("")