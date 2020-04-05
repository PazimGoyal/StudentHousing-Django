from django import forms
from .models import SignUpModel


class MyForm(forms.ModelForm):
    class Meta:
        model = SignUpModel
        fields = "__all__"
