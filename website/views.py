from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.views.decorators.cache import cache_page
from django.template import RequestContext, loader

from models import HauntedLocation, HauntedLocationDescription

#@cache_page(60 * 1)
def index(request):
    haunted_location_list = HauntedLocation.objects.all()



    context = {'haunted_location_list': haunted_location_list}

    return render(request, 'website/index.html', context)

#@cache_page(60 * 1)
def detail(request, slug, id):
    print(id)
    print(slug)
    haunted_location = get_object_or_404(HauntedLocation, pk=id)
    try:
        haunted_location_description = get_object_or_404(HauntedLocationDescription, pk=id)
    except Http404:
        haunted_location_description =""

    print(type(haunted_location_description))

    context = {'haunted_location':haunted_location,'haunted_location_description':haunted_location_description}

    return render(request, 'website/detail.html', context)

# Create your views here.
