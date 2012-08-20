# -*- coding: utf-8 -*-

"""
settings.py
   django settings.
"""

#################################################
# IMPORTS
#################################################
from django.conf import settings

#urllib2.ProxyHandler dictionary
DEFAULT_SQUID_CONFIG = {
        'http' : 'http://localhost:3128',
        'https' : 'http://localhost:3128'
}

# Set to false to use django cache instead.  Must be configured via app
# settings.py
DEFAULT_USE_SQUID = True

SQUID_CONFIG = getattr(settings, 'SQUID_CONFIG',
    DEFAULT_SQUID_CONFIG)

USE_SQUID = getattr(settings, 'USE_SQUID',
    DEFAULT_USE_SQUID)

