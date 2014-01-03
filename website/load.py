__author__ = 'derya'
import os
from django.contrib.gis.utils import LayerMapping
from models import HauntedLocation
from models import HauntedLocation_mapping

HauntedLocations_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'haunted_locations/haunted_locations.shp'))

def run(verbose=True):
    lm = LayerMapping(HauntedLocation, HauntedLocations_shp, HauntedLocation_mapping,
                      transform=False, encoding='iso-8859-1')

    lm.save(strict=True, verbose=verbose)


