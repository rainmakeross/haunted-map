__author__ = 'derya'

from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from external_data.views import YouTubeSearchJSONView

urlpatterns = patterns('',



    url(r'^youtube_search/(?P<query>[-\w\d]+),(?P<max_results>[-\w\d]+)$$', YouTubeSearchJSONView.as_view(), name="YouTubeSearchJSONView"),


)
