# -*- coding: utf-8 -*-

"""
RCS Info:
   $Id: views.py 1340 2012-05-15 15:07:17Z jbrown $

   Last Revised    :  $Date: 2012-05-15 09:07:17 -0600 (Tue, 15 May 2012) $
   By              :  $Author: jbrown $
   Rev             :  $Rev: 1340 $

TODO:
  - Default copyright notice
  - Config file for directory paths

"""

# pylint -- name convention
#pylint: disable-msg=C0103
# pylint -- undefined variables.  Sometimes we return local()
#pylint: disable-msg=E0602

from django.http import HttpResponse, HttpResponseForbidden, \
        HttpResponseServerError
from models import WhiteListedURLs

from util import sessionlessProxyFetch



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
        return HttpResponseForbidden('Requested Resource Denied')

    try:
        spf = sessionlessProxyFetch(myURL)
    except:
        raise HttpResponseServerError('Unknown problem proxying Resource')

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
