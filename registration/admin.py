from django.contrib import admin
from .models import RegistrationModel

# Register your models here.

@admin.register(RegistrationModel)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name']
    search_fields = ['first_name','last_name']
