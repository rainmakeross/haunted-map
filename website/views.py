from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from django.views.generic import DetailView
from django.http import HttpResponse, Http404
from django.views.decorators.cache import cache_page
from django.template import RequestContext, loader

from models import HauntedLocation, HauntedLocationDescription

#@cache_page(60 * 1)
class Index(View):
    template_name = 'website/index.html';
    def get(self,request):

        haunted_location_list = HauntedLocation.objects.all()


        context = {'haunted_location_list': haunted_location_list}

        return render(request, self.template_name, context)

class HauntedLocationList(ListView):
    model = HauntedLocation

#@cache_page(60 * 1)
class HauntedLocationDetail(DetailView):
    model = HauntedLocation
    context_object_name = 'haunted_location'

    def get_object(self, queryset=None):
        obj = super(HauntedLocationDetail, self).get_object(queryset)
        try:
            self.description = get_object_or_404(HauntedLocationDescription, haunted_location = obj.id)
        except Http404:
            self.description = "Not Found"
        return obj

    def get_context_data(self, **kwargs):

        # Call the base implementation first to get a context
        context = super(HauntedLocationDetail, self).get_context_data(**kwargs)
        # Add in HTML content
        context['haunted_location_description'] = self.description
        return context







# Create your views here.
