__author__ = 'derya'

from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from views import Index, HauntedLocationList, HauntedLocationDetail, AboutUs, HowItWorks, YouTubeSearchPartialView

urlpatterns = patterns('',


    url(r'^$', Index.as_view(), name="HauntedIndex"),
    url(r'^locations/$', HauntedLocationList.as_view(), name="HauntedLocationList"),
    url(r'^detail/(?P<slug>[-\w\d]+),(?P<pk>\d+)$', HauntedLocationDetail.as_view(), name='HauntedLocationDetail'),
    url(r'^about_us$',AboutUs.as_view(), name='AboutUs'),
    url(r'^how_it_works$',HowItWorks.as_view(), name='HowItWorks'),
    url(r'^test$',YouTubeSearchPartialView.as_view(), name='test')


)
