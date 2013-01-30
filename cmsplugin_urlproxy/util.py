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
def sessionlessProxyFetch(url, timeout=urlproxy_settings.REQUEST_TIMEOUT):
    """
    Fetch a URL from our configured proxy server.
    >>> data = sessionlessProxyFetch('http://www.example.com')
    >>> data.read()[:20]
    '<!DOCTYPE html PUBLI'
    """
    if urlproxy_settings.USE_SQUID:
        return __squidProxyFetch(url, timeout)
    else:
        return __cacheProxyFetch(url, timeout)
#------------------------------------------------------------------------

#------------------------------------------------------------------------
def __cacheProxyFetch(url, timeout):
    """
    Fetch a URL from the django cache.  Least preferred.

    Mocks parts of a urllib2.opener object
    """

    from StringIO import StringIO
    from django.core.cache import cache

    key = urlproxy_settings.CACHE_PREFIX + url

    class FakeURLLibOpener():
        """
        views.py ultimately expects to mock a content-type, and a result
        to read.
        """
        def __init__(self, headers, data):
            self.data = StringIO(data)
            self.headers = headers

        def info(self):
            return self

        def read(self):
            return self.data.read()

    if not cache.has_key(key):
        opener = urllib2.build_opener()
        data = opener.open(url, None, timeout)

        toStore = {
            'headers' : data.info().headers,
            'data' : data.read()
        }
        cache.set(key, toStore)

        return FakeURLLibOpener(** toStore)
        # The same object we save in the cache, returned because on systems
        # configured with a fake cache, cache.get always returns None

    # Wrap in file-like now that we have it.
    return FakeURLLibOpener(** cache.get(key))
#------------------------------------------------------------------------


#------------------------------------------------------------------------
def __squidProxyFetch(url, timeout):
    """
    Fetch a URL from SQUID.  Assumes Squid properly configured.
    """
    opener = urllib2.build_opener(
        urllib2.ProxyHandler(urlproxy_settings.SQUID_CONFIG)
    )
    return opener.open(url, None, timeout)
#------------------------------------------------------------------------

if __name__ == "__main__":
    import doctest
    doctest.testmod()
