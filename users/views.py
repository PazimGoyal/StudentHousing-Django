from django.http import HttpResponse
from django.shortcuts import render
from .forms import MyForm


# Create your views here.
def signup(request):
    ans='null'
    form = MyForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
    return render(request, 'signUp.html', {'form': form,'ans':ans})
