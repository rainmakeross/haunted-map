from django.contrib import admin
from django.contrib.gis import admin
from models import HauntedLocation
from models import Country
from models import State
from models import Category
from models import HauntedLocationDescription


class CountryAdmin(admin.ModelAdmin):
    field=['country_name']

admin.site.register(HauntedLocation, admin.OSMGeoAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(State)
admin.site.register(Category)
admin.site.register(HauntedLocationDescription)


# Register your models here.
