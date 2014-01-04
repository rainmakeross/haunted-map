
from django.template.defaultfilters import slugify

# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models
class Country(models.Model):
    def __unicode__(self):
        return self.country_name
    country_name = models.CharField(max_length=255)

class State(models.Model):
    def __unicode__(self):
        return self.state_name
    state_name = models.CharField(max_length=255)
    country = models.ForeignKey(Country)

class Category(models.Model):
    def __unicode__(self):
        return self.category_name
    category_name = models.CharField(max_length=255)
    presentation_name = models.CharField(max_length=255)

class  HauntedLocation(models.Model):
    def __unicode__(self):
        return self.name

    def _url(self):
        super(HauntedLocation, self).save()

        url = '%s,%s' % (
             slugify(self.name),slugify(self.id)
        )
        return url
    slug = property(_url)

    @models.permalink
    def get_absolute_url(self):
        return ('HauntedLocationDetail', (slugify(self.name), slugify(self.id)))

    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    category = models.CharField(max_length=255)
    geom = models.MultiPointField(srid=4326)
    objects = models.GeoManager()

class HauntedLocationDescription(models.Model):
    def __unicode__(self):
        return self.html_content
    haunted_location = models.ForeignKey(HauntedLocation, unique=True)
    html_content = models.TextField()



# Auto-generated `LayerMapping` dictionary for  --srid=4326 model
HauntedLocation_mapping = {
    'name' : 'name',
    'latitude' : 'latitude',
    'longitude' : 'longitude',
    'category' : 'category',
    'geom' : 'MULTIPOINT',
}


# Create your models here.
