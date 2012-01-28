# -*- coding: utf-8 -*-
import datetime

from piston.handler import BaseHandler
from piston.utils import rc
from piston.doc import generate_doc

from core.models import Device, DeviceLocation

from googlemaps import GoogleMaps, GoogleMapsError


class DeviceLocationHandler(BaseHandler):
    """DeviceLocation handler class for the RESTful API."""
    allowed_methods = ('POST',)
    model = DeviceLocation
    fields = ('device_name', 'device_id', 'lat', 'lon')

    @classmethod
    def content_length(cls, devicelocation):
        return len(devicelocation.content)

    @classmethod
    def resource_uri(cls, devicelocation):
        return ('devicelocation', ['json', ])

    def read(self, request):
        return {}

    def create(self, request):
        """Add a new device location."""
        attrs = self.flatten_dict(request.POST)

        try:
            device = Device.objects.get(user=request.user, name=attrs['device_name'], mobile_id=attrs['device_id'])
        except Device.DoesNotExist:
            return rc.NOT_FOUND

        gmaps = GoogleMaps()
        try:
            address = gmaps.latlng_to_address(float(attrs['lat']), float(attrs['lon']))
        except GoogleMapsError:
            address = None

        device_location = DeviceLocation(device=device,
                                         address=address,
                                         lat=float(attrs['lat']),
                                         lon=float(attrs['lon']),
                                         created=datetime.datetime.now())
        device_location.save()

        return rc.CREATED


doc = generate_doc(DeviceLocationHandler)
