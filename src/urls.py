from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

from jsonrpc import jsonrpc_site
import core.views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^json/browse/', 'jsonrpc.views.browse', name="jsonrpc_browser"),
    url(r'^json/', jsonrpc_site.dispatch, name="jsonrpc_mountpoint"),
    (r'^json/(?P<method>[a-zA-Z0-9.]+)$', jsonrpc_site.dispatch),
)