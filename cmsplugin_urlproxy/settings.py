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

# 5 seconds -- Note, this update now requires python2.6
#  it could be worked around via monkeypatching socket.settimeout,
#  but I have not yet confirmed if that is threadsafe
DEFAULT_REQUEST_TIMEOUT = 5
REQUEST_TIMEOUT = getattr(settings, 'REQUEST_TIMEOUT',
    DEFAULT_REQUEST_TIMEOUT)

