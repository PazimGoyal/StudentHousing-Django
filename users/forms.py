from django import forms

from .models import UserModel
from django.contrib.auth.models import User

class myForm(forms.ModelForm):
    class Meta:
        model = UserModel
        exclude = ['user']
class editProfie(forms.ModelForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email"]
