from django.contrib import admin

from .models import Pets
@admin.register(Pets)
class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'breed', 'species', 'sex', 'age']

