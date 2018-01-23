# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User

def home(request):
    print request.COOKIES
    return HttpResponse("as")

def verify_session(request, ses):
    try:
        ses_obj = Session.objects.get(session_key=ses)
        uid = ses_obj.get_decoded().get('_auth_user_id')
        return HttpResponse(uid)
    except:
        return HttpResponse(0)