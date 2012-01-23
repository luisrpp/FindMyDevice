# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response


def homepage(request, template=None):
    context = RequestContext(request)
    return render_to_response(template, context)
