# -*- coding: utf-8 -*-

"""
settings.py
   django settings

RCS Info:
   $Id: settings.py 1340 2012-05-15 15:07:17Z jbrown $

   Last Revised    :  $Date: 2012-05-15 09:07:17 -0600 (Tue, 15 May 2012) $
   By              :  $Author: jbrown $
   Rev             :  $Rev: 1340 $

TODO:
  - Default copyright notice
"""

#################################################
# IMPORTS
#################################################
from django.conf import settings


# TODO: available via settings.py
DEFAULT_SQUID_CONFIG = {
        'http' : 'http://localhost:3128',
        'https' : 'http://localhost:3128'
}

SQUID_CONFIG = getattr(settings, 'SQUID_CONFIG',
    DEFAULT_SQUID_CONFIG)

if settings.DEBUG:
    SQUID_CONFIG = None
    # Disabled for testing / development.


