from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    (r'^$', 'core.views.homepage', {'template': 'index.html'}),
    (r'^api/', include('api.urls')),
)

urlpatterns += staticfiles_urlpatterns()
