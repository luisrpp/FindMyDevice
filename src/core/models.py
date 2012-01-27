# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User

import string
import random


def id_generator(size=9, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


class Device(models.Model):
    """Class that represents the mobile device"""
    user = models.ForeignKey(User, verbose_name=_(u'User'))
    name = models.CharField(verbose_name=_(u'Name'), max_length=40)
    description = models.CharField(verbose_name=_(u'Description'), max_length=100)
    mobile_id = models.CharField(verbose_name=_(u'Mobile identifier'), max_length=9, default=id_generator)

    class Meta:
        ordering = ['name']
        verbose_name = _(u'Device')
        verbose_name_plural = _(u'Devices')

    def __unicode__(self):
        return self.name


class DeviceLocation(models.Model):
    """Class that represents the mobile device location"""
    device = models.ForeignKey(Device, verbose_name=_(u'Device'))
    address = models.CharField(verbose_name=_(u'Address'), max_length=255, null=False, blank=False)
    lat = models.DecimalField(verbose_name=_(u'Latitude'), max_digits=10, decimal_places=7)
    lon = models.DecimalField(verbose_name=_(u'Longitude'), max_digits=10, decimal_places=7)
    created = models.DateTimeField(verbose_name=_(u'Date of occurrence'))

    class Meta:
        ordering = ['device', '-created']
        verbose_name = _(u'Device Location')
        verbose_name_plural = _(u'Devices Locations')

    def __unicode__(self):
        return self.device.name
