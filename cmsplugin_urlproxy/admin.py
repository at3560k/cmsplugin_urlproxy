#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
admin.py
"""

from django.conf import settings as settings
from django.contrib import admin
from cmsplugin_urlproxy import models

import sys
import inspect

class MYWhiteListedURLsAdmin(admin.ModelAdmin):
    """
    White List URLs for CMS Proxy.  Admin Editor.
    """
    model = models.WhiteListedURLs
    display = True
    search_fields = ('allowed_url',)
    list_display = ('allowed_url',)


#################################################
# Inspection loading modules: Show all admin classes
#################################################
current_module = sys.modules[__name__]
for name, obj in inspect.getmembers(sys.modules[__name__], inspect.isclass):
    if getattr(obj, 'display', settings.DEBUG):
        admin.site.register(obj.model, obj)


