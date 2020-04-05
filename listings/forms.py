from django import forms
from .models import HouseListings


class SaveData(forms.ModelForm):
    class Meta:
        model = HouseListings
        fields = "__all__"
