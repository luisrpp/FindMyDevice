# -*- coding: utf-8 -*-
from core.models import Device


def sidebar_devices(request):
    """Sidebar context processor"""
    if request.user.id != None:
        devices = Device.objects.filter(user=request.user)
        return {'devices': devices}
    return {}
