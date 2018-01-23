# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Urly(models.Model):
    user = models.CharField(max_length=255)
    original_url = models.TextField()
    org = models.CharField(max_length=20)
    short_url = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.short_url
