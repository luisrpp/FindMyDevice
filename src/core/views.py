# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    context = RequestContext(request)
    return render_to_response('profile.html', context)


@login_required
def add_device(request):
    context = RequestContext(request)
    return render_to_response('profile.html', context)
