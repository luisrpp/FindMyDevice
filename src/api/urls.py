from django.conf.urls.defaults import *

from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication
from piston.doc import documentation_view

from api.handlers import DeviceLocationHandler


auth = HttpBasicAuthentication(realm='FindMyDevice API')

devicelocation = Resource(handler=DeviceLocationHandler, authentication=auth)

urlpatterns = patterns('',
    url(r'^location/$', devicelocation),
    url(r'^location/(?P<emitter_format>.+)/$', devicelocation),
    url(r'^location\.(?P<emitter_format>.+)', devicelocation, name='devicelocation'),

    # automated documentation
    url(r'^$', documentation_view),
)
