from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.views.generic import ListView, DetailView, TemplateView, FormView
from django.template.defaultfilters import slugify
from forms import SearchForm
from django.views.generic.edit import ProcessFormView

import json


from django.http import HttpResponse, Http404
from django.views.decorators.cache import cache_page
from django.template import RequestContext, loader

from models import HauntedLocation, HauntedLocationDescription


class JSONResponseMixin(object):
    """
    A mixin that can be used to render a JSON response.
    """
    def render_to_json_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        return HttpResponse(
            self.convert_context_to_json(context),
            content_type='application/json',
            **response_kwargs
        )

    def convert_context_to_json(self, context):
        "Convert the context dictionary into a JSON object"
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        return json.dumps(context)


#@cache_page(60 * 1)
class Index(View):
    template_name = 'website/index.html'
    def get(self,request):

        haunted_location_list = HauntedLocation.objects.all()


        context = {'haunted_location_list': haunted_location_list}

        return render(request, self.template_name, context)

class AboutUs(TemplateView):
    template_name = 'website/about_us.html'

class HowItWorks(TemplateView):
    template_name = 'website/how_it_works.html'


class HauntedLocationSearch(ListView):
    template_name = 'website/hauntedlocation_search.html'
    context_object_name = 'haunted_location_list'

    model = HauntedLocation

    # def post(self, request, *args, **kwargs):
    #     context ={'results':"1"}
    #     if(request.POST["query"]):
    #         query = request.POST["query"]
    #         print request.POST["query"]
    #         haunted_location_list = HauntedLocation.objects.filter(name__icontains=query)
    #         context ={'results': haunted_location_list}
    #     print context
    #     return HttpResponse(context)
    #
    #
    # def get(self, request, *args, **kwargs):
    #     return render(request,self.template_name,self.context)

    def get_queryset(self):
        if self.request.REQUEST.get("query"):
            self.query = self.request.REQUEST.get("query");
            self.search_obj = HauntedLocation.objects.filter(name__icontains=self.query)
        return HauntedLocation.objects.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(HauntedLocationSearch, self).get_context_data(**kwargs)
        # Add in the publisher
        if hasattr(self, 'query'):
            context['search_results'] = self.search_obj

        return context




#@cache_page(60 * 1)
class HauntedLocationDetail(DetailView):
    model = HauntedLocation
    context_object_name = 'haunted_location'


    def get_object(self, queryset=None):
        obj = super(HauntedLocationDetail, self).get_object(queryset)
        self.wikipedia_name = obj.name
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
        context['haunted_location_youtube_name'] = slugify(self.wikipedia_name)
        context['haunted_location_wikipedia_name'] = self.wikipedia_name.replace(" ","_").replace("'","%27")

        return context




class TestView(TemplateView):
    template_name = 'website/test.html'








