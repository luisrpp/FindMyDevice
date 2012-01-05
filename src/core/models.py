# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User

class Device(models.Model):
    """Class that represents the mobile device"""
    user               = models.ForeignKey(User, verbose_name=_(u'User'))
    device_name        = models.CharField(verbose_name=_(u'Name'), max_length=40)
    device_description = models.CharField(verbose_name=_(u'Description'), max_length=100)
    device_mobile_id   = models.CharField(verbose_name=_(u'Mobile identifier'), max_length=9)

    class Meta:
        ordering            = ['device_name']
        verbose_name        = _(u'Device')
        verbose_name_plural = _(u'Devices')
    
    def __unicode__(self):
        return self.name

class DeviceLocation(models.Model):
    """Class that represents the mobile device location"""
    device  = models.ForeignKey(Device, verbose_name=_(u'Device'))
    lat = models.DecimalField(verbose_name='Latitude', max_digits=8, decimal_places=2)
    lon = models.DecimalField(verbose_name='longitude', max_digits=8, decimal_places=2)
    created = models.DateTimeField(verbose_name=_(u'Date of occurrence'))

    class Meta:
        ordering            = ['device', '-created']
        verbose_name        = _(u'Device Location')
        verbose_name_plural = _(u'Devices Locations')
    
    def __unicode__(self):
        return self.device.name