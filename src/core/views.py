# -*- coding: utf-8 -*-
from jsonrpc import jsonrpc_method
from core.models import Device, DeviceLocation

@jsonrpc_method('FindMyDevice.add_location')
def add_location(request, username, device_id, lat, lon):
    return {'status': 'success'}