# -*- coding: utf-8 -*-
from django import forms

from core.models import Device


class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        exclude = ('user', 'mobile_id')

    def save(self, user, commit=True, *args, **kwargs):
        device = super(DeviceForm, self).save(commit=False, *args, **kwargs)
        device.user = user
        if commit:
            device.save()
        return device
