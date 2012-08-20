# -*- coding: utf-8 -*-

"""
utilities.py
   Utility/wrapper functions
"""

import urllib2
from cmsplugin_urlproxy import settings as urlproxy_settings


#################################################
#      Public Functions
#################################################

#------------------------------------------------------------------------
def sessionlessProxyFetch(url):
    """
    Fetch a URL from our configured proxy server.
    >>> data = sessionlessProxyFetch('http://www.example.com')
    >>> data.read()[:20]
    '<!DOCTYPE html PUBLI'
    """
    if urlproxy_settings.USE_SQUID:
        return __squidProxyFetch(url)
    else:
        return __cacheProxyFetch(url)
#------------------------------------------------------------------------

#------------------------------------------------------------------------
def __cacheProxyFetch(url):
    """
    Fetch a URL from the django cache.  Least preferred.
    """

    from StringIO import StringIO
    from django.core.cache import cache

    if not cache.has_key(url):
        opener = urllib2.build_opener()
        data = opener.open(url)
        cache.set(url, data.read() )

    # Wrap in file-like now that we have it.
    return StringIO(cache.get(url))

#------------------------------------------------------------------------


#------------------------------------------------------------------------
def __squidProxyFetch(url):
    """
    Fetch a URL from SQUID.  Assumes Squid properly configured.
    """
    opener = urllib2.build_opener(
        urllib2.ProxyHandler(urlproxy_settings.SQUID_CONFIG)
    )
    return opener.open(url)
#------------------------------------------------------------------------

if __name__ == "__main__":
    import doctest
    doctest.testmod()
