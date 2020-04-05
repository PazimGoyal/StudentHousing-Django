from django.http import HttpResponse
from django.shortcuts import render
from .forms import MyForm


# Create your views here.
def signup(request):
    form = MyForm(request.POST)
    if form.is_valid():
        form.save()
    return render(request, 'signUp.html', {'form': form})
