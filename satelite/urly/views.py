# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import urllib2
from django.shortcuts import render
from django.http import HttpResponse
from .models import Urly

def urly(request, url):
    s = request.COOKIES.get("sessionid")
    response = urllib2.urlopen('http://localhost:8000/verify/%s' % s )
    user = response.read()
    if user != "0":
        try :
            urly = Urly.objects.get(user=user, short_url=url)
            return HttpResponse("URL nya adalah: %s" % urly.original_url )
        except:
            return HttpResponse("Error cuk !!!!")
    else:
        return HttpResponse("Kamu belum login")
