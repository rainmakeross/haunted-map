from django.contrib import admin
from django.contrib.gis import admin
from models import HauntedLocation, Country, State, Category, HauntedLocationDescription, TvShow


class CountryAdmin(admin.ModelAdmin):
    field=['country_name']

admin.site.register(HauntedLocation, admin.OSMGeoAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(State)
admin.site.register(Category)
admin.site.register(HauntedLocationDescription)
admin.site.register(TvShow)


# Register your models here.
