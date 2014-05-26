from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView, TemplateView, CreateView

__author__ = 'derya'

from django.conf.urls import patterns, url
from django.template.defaultfilters import register
from django.views.decorators.http import require_http_methods, require_POST, require_GET
from django.views.decorators.cache import cache_page

from views import Index, HauntedLocationSearch, HauntedLocationDetail, AboutUs, HowItWorks, TestView, HauntedEpisodeGuide
from models import Newsletter, Comment

urlpatterns = patterns('',


    url(r'^$', cache_page(60 * 1)(Index.as_view()), name="HauntedIndex"),
    url(r'^detail/(?P<slug>[-\w\d]+),(?P<pk>\d+)$', HauntedLocationDetail.as_view(), name='HauntedLocationDetail'),
    url(r'^about_us$',AboutUs.as_view(), name='AboutUs'),
    url(r'^how_it_works$',HowItWorks.as_view(), name='HowItWorks'),
    url(r'^test$',TestView.as_view(), name='test'),
    url(r'^episode_guide',HauntedEpisodeGuide.as_view(), name='HauntedEpisodeGuide'),
    #GET Form returns
    url(r'^search$',HauntedLocationSearch.as_view(), name='HauntedLocationSearch'),
    #POST Form returns
    url(r'^newsletter$',require_POST(CreateView.as_view(model=Newsletter, success_url="/website/", template_name="website/partial/_dummy.html")), name='NewsletterView' ),
    url(r'^comment$',CreateView.as_view(model=Comment, success_url="/website/",template_name="website/partial/_dummy.html"), name='CommentView' ),


)
