# -*- coding: utf-8 -*-

"""
settings.py
   django settings for cmsplugin_urlproxy module.
"""

#################################################
# IMPORTS
#################################################
import os
from django.conf import settings

#urllib2.ProxyHandler dictionary
DEFAULT_SQUID_CONFIG = {
        'http' : 'http://localhost:3128',
        'https' : 'http://localhost:3128'
}

# Set to false to use django cache instead.  Must be configured via app
# settings.py
DEFAULT_USE_SQUID = True

DEFAULT_PROXY_CACHE_PREFIX = os.path.dirname(__file__)

SQUID_CONFIG = getattr(settings, 'SQUID_CONFIG',
    DEFAULT_SQUID_CONFIG)

USE_SQUID = getattr(settings, 'USE_SQUID',
    DEFAULT_USE_SQUID)

CACHE_PREFIX = getattr(settings, 'PROXY_CACHE_PREFIX',
    DEFAULT_PROXY_CACHE_PREFIX)
