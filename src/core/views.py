# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from core.models import Device
from core.forms import DeviceForm


@login_required
def profile(request):
    context = RequestContext(request)
    return render_to_response('profile.html', context)


@login_required
def add_device(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)


@login_required
def new(request):
    form = DeviceForm()
    context = RequestContext(request, {'form': form})
    return render_to_response('core/add_device.html', context)


@login_required
def create(request):
    form = DeviceForm(request.POST)

    if not form.is_valid():
        context = RequestContext(request, {'form': form})
        return render_to_response('core/add_device.html', context)

    device = form.save(request.user)

    return HttpResponseRedirect(reverse('core:success_device', args=[device.pk]))


@login_required
def success_device(request, pk):
    device = get_object_or_404(Device, pk=pk, user=request.user)
    context = RequestContext(request, {'device': device})
    return render_to_response('core/success_device.html', context)


@login_required
def device(request, pk):
    device = get_object_or_404(Device, pk=pk, user=request.user)
    context = RequestContext(request, {'device': device})
    return render_to_response('core/device.html', context)
