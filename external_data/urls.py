__author__ = 'derya'

from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from views import YoutubeSearchView

urlpatterns = patterns(



    url(r'^youtube_search/$', YoutubeSearchView.as_view()),


)
