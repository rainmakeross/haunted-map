from django.conf.urls import patterns, include, url



from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^website/', include('website.urls')),
    url(r'^external_data/', include('external_data.urls')),
    url(r'^admin/', include(admin.site.urls)),

)
