__author__ = 'derya'

from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from views import Index, HauntedLocationList, HauntedLocationDetail

urlpatterns = patterns('',


    url(r'^$', Index.as_view()),
    url(r'^locations/$', HauntedLocationList.as_view()),
    url(r'^detail/(?P<slug>[-\w\d]+),(?P<pk>\d+)$', HauntedLocationDetail.as_view(), name='HauntedLocationDetail'),

)
