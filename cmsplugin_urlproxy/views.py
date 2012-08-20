# -*- coding: utf-8 -*-

"""
views.py

Defines Proxy Fetching routine
"""

# pylint -- name convention
#pylint: disable-msg=C0103
# pylint -- undefined variables.  Sometimes we return local()
#pylint: disable-msg=E0602

from django.http import HttpResponse, HttpResponseForbidden, \
        HttpResponseServerError

from django.utils.translation import ugettext_lazy as _

from cmsplugin_urlproxy.models import WhiteListedURLs
from cmsplugin_urlproxy.util import sessionlessProxyFetch



#################################################
#      Web Available Functions
#################################################

#------------------------------------------------------------------------
def SSLProxyFetch(request, proto, resource):
    """
    I have been called with /secure/some/url.stuff

    - My primary duty is to listen on a url, and fetch and return the requested
      file.
    - My secondary duty is to make sure that the file in question is
      whitelisted...  I'm not exposing a blind web proxy!

    But on a production server, I will be listening on SSL and thus provide it.
    """

    myURL = proto + '://' + resource

    try:
        WhiteListedURLs.objects.get(allowed_url = myURL)
    except WhiteListedURLs.DoesNotExist:
        return HttpResponseForbidden(_('Requested Resource Denied'))

    try:
        spf = sessionlessProxyFetch(myURL)
    except:
        raise HttpResponseServerError(_('Unknown problem proxying Resource'))

    headers = spf.info().headers
    headers_d = dict(
        [i.strip().split(': ') for i in headers]
    )

    if 'Content-Type' in headers_d:
        response = HttpResponse(mimetype=headers_d['Content-Type'])
    else:
        response = HttpResponse()

    data = spf.read()
    response.write(data)
    return response
#------------------------------------------------------------------------
