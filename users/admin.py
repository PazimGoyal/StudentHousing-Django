from django.contrib import admin
from .models import SignUpModel


# Register your models here.


class SignUpmodelAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'mobile', 'email')


admin.site.register(SignUpModel, SignUpmodelAdmin)
