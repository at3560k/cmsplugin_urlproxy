# -*- coding: utf-8 -*-

"""
utilities.py
   Utility/wrapper functions

RCS Info:
   $Id: util.py 1340 2012-05-15 15:07:17Z jbrown $

   Last Revised    :  $Date: 2012-05-15 09:07:17 -0600 (Tue, 15 May 2012) $
   By              :  $Author: jbrown $
   Rev             :  $Rev: 1340 $

TODO:
  - Default copyright notice
  - Config file for directory paths

"""

import urllib2
import cookielib
import os

# this plugin's settings
import settings as mySet


#################################################
#      Public Functions
#################################################

#------------------------------------------------------------------------
def sessionlessProxyFetch(url):
    """
    Fetch a URL from our proxy server.  Should be very fast and avoid caching
    issues.  Note, this doesn't use IBIS cookies...

    >>> data = sessionlessProxyFetch('http://www.example.com')
    >>> data.read()[:20]
    '<!DOCTYPE html PUBLI'
    """
    opener = urllib2.build_opener(__myProxyHandler())
    return opener.open(url)
#------------------------------------------------------------------------

#------------------------------------------------------------------------
def proxyFetch(cjLocation, url):
    """
    Fetch URL from the proxy server, but point at a cookiejar
    cjLocation: str: /path/to/my/cookiejar file
    url : str : the URL
    """

    cj = cookielib.MozillaCookieJar()

    if os.path.isfile(cjLocation):
        cj.load(cjLocation, ignore_discard=True)
        # Yeah Python, let's just throw out session cookies because it's
        # easier by default

    opener = urllib2.build_opener(
        urllib2.HTTPCookieProcessor(cj),
        __myProxyHandler(),
        urllib2.HTTPRedirectHandler
    )
    result = opener.open(url)
    cj.save(cjLocation, ignore_discard=True)
    return result
#------------------------------------------------------------------------

#################################################
#      Private Functions
#################################################

#------------------------------------------------------------------------
def __myProxyHandler():
    return urllib2.ProxyHandler(mySet.SQUID_CONFIG)
#------------------------------------------------------------------------

