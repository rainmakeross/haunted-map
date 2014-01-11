__author__ = 'derya'

from django.conf.urls import patterns, url
from django.views.decorators.http import require_http_methods, require_POST, require_GET

from views import Index, HauntedLocationSearch, HauntedLocationDetail, AboutUs, HowItWorks, TestView

urlpatterns = patterns('',


    url(r'^$', Index.as_view(), name="HauntedIndex"),
    url(r'^detail/(?P<slug>[-\w\d]+),(?P<pk>\d+)$', HauntedLocationDetail.as_view(), name='HauntedLocationDetail'),
    url(r'^about_us$',AboutUs.as_view(), name='AboutUs'),
    url(r'^how_it_works$',HowItWorks.as_view(), name='HowItWorks'),
    url(r'^test$',TestView.as_view(), name='test'),
    #JSON returns
    url(r'^search$',HauntedLocationSearch.as_view(), name='HauntedLocationSearch'),


)
