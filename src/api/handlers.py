# -*- coding: utf-8 -*-
import datetime

from piston.handler import BaseHandler
from piston.utils import rc

from core.models import Device, DeviceLocation


class DeviceLocationHandler(BaseHandler):
    """DeviceLocation handler class for the RESTful API."""
    model = DeviceLocation
    fields = ('device_name', 'device_id', 'lat', 'lon')

    @classmethod
    def content_length(cls, devicelocation):
        return len(devicelocation.content)

    @classmethod
    def resource_uri(cls, devicelocation):
        return ('devicelocation', ['json', ])

    def create(self, request):
        """Add a new device location."""
        attrs = self.flatten_dict(request.POST)

        try:
            device = Device.objects.get(user=request.user, name=attrs['device_name'], mobile_id=attrs['device_id'])
        except Device.DoesNotExist:
            return rc.NOT_FOUND

        device_location = DeviceLocation(device=device,
                                         lat=int(attrs['lat']),
                                         lon=int(attrs['lon']),
                                         created=datetime.datetime.now())
        device_location.save()

        return rc.CREATED
