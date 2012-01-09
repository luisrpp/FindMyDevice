# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.utils import simplejson
from django.contrib.csrf.middleware import csrf_exempt

def add_location(request):
    print request
    if request.is_ajax():
        message = "Hello AJAX"
        print "Hello AJAX"
    else:
        message = "Hello"
    return HttpResponse(message, mimetype='application/json')
add_location = csrf_exempt(add_location)