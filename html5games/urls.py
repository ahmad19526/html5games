from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

from ajax_select import urls as ajax_select_urls

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    
    # url(r'^$', 'html5games.views.home', name='home'),
    # url(r'^html5games/', include('html5games.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/lookups/', include(ajax_select_urls)),
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^dasdemo/', include('dasdemo.urls')),
    url(r'^typeahead/', include('typeahead.urls')),
    url(r'^adam/', include('adam.urls')),
    url(r'^jcrop/', include('jcrop.urls')),
)
