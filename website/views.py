from urllib2 import urlopen
from xml.dom import minidom
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from django.template.defaultfilters import slugify, register


import json


from django.http import HttpResponse, Http404


from models import HauntedLocation, HauntedLocationDescription, TvShow




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

class HauntedEpisodeGuide(ListView):
    model = TvShow
    template_name = 'website/episode_guide.html'
    context_object_name = 'tvshows'

    TVDB_API_KEY = '9036B99877C335CD'
    url_base = 'http://thetvdb.com/api/'
    url = url_base +TVDB_API_KEY+'/series/125391/all/'



    def get_queryset(self):
        if self.request.REQUEST.get("id"):
            self.query_id = self.request.REQUEST.get("id");
            try:
                search_obj = get_object_or_404(TvShow, id=self.query_id)
                self.tvdb_id = str(search_obj.tvdb_id)
            except Http404:
                self.tvdb_id = None
        return TvShow.objects.all()

    def get_context_data(self, **kwargs):
        #Calling the base implementation for context
        context = super(HauntedEpisodeGuide, self).get_context_data(**kwargs)
        # Get Episodes Return
        try:
            context['episodes_list'] = self.get_episodes(self.tvdb_id)
        except Exception as e:
            print 'episode server problem' + str(e)
        if self.request.REQUEST.get("id"):
            try:
                context['query_id'] = int(self.query_id)
                print self.query_id
            except:
                print 'no query selected'
        return context

    def get_episodes(self,series_id):
        episodes_list = []


        self.url = self.url_base + self.TVDB_API_KEY+'/series/'+series_id+'/all/'
        xml_doc = urlopen(self.url)
        parsed_xml = minidom.parse(xml_doc)
        episodes = parsed_xml.getElementsByTagName("Episode")
        for episode in episodes:
            episode_dict = {}
            episode_name = episode.getElementsByTagName("EpisodeName")[0].firstChild.data
            episode_id = episode.getElementsByTagName("id")[0].firstChild.data
            episode_number = episode.getElementsByTagName("EpisodeNumber")[0].firstChild.data
            season_number = episode.getElementsByTagName("SeasonNumber")[0].firstChild.data
            language = episode.getElementsByTagName("Language")[0].firstChild.data
            try:
                overview = episode.getElementsByTagName("Overview")[0].firstChild.data
            except:
                overview =''
            episode_dict = dict(episode_name=episode_name,episode_id=episode_id, episode_number=episode_number, season_number=season_number,language=language, overview=overview)
            episodes_list.append(episode_dict)
        return episodes_list










