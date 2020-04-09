from django.contrib import messages, auth
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from listings.models import HouseListings
from .models import UserModel


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
    myobject = HouseListings.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'items': myobject})


def register(request):
    if request.method == 'POST':
        form = User(request.POST)
        form2 = UserModel(request.POST, request.FILES)
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
                    messages.success(request, "Account Successfully Created")
                    return redirect("login")
        else:
            messages.error(request, "Passwords Do Not Match")
    else:
        form = User()
        form2 = UserModel()

    return render(request, 'register.html', {'form': form, 'form2': form2})
