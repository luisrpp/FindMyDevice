# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

from core.models import Device


def homepage(request, template=None):
    context = RequestContext(request)
    return render_to_response(template, context)


@login_required
def profile(request):
    devices = Device.objects.filter(user=request.user)
    context = RequestContext(request, {'devices': devices})
    return render_to_response('profile.html', context)


@login_required
def add_device(request):
    context = RequestContext(request)
    return render_to_response('profile.html', context)
