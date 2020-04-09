from django import forms

from .models import UserModel


class myForm(forms.ModelForm):
    class Meta:
        model = UserModel
        exclude = ['user']
