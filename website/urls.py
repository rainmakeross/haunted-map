__author__ = 'derya'

from django.conf.urls import patterns, url
from website.views import detail
from django.views.generic import TemplateView

from website import views

urlpatterns = patterns('',

    url(r'^', 'website.views.index'),
    url(r'^location/', 'website.views.index'),
    url(r'^detail/([-\w\d]+),(\d+)$', 'website.views.detail'),
    #url(r'^detail/(?P<slug>[-\w\d]+),(?P<id>\d+)/$', view=detail, name='detail'),
)
