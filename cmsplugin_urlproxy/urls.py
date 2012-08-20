#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
urls.py

RCS Info:
   $Id: urls.py 1244 2012-03-29 18:01:22Z jbrown $

   Last Revised    :  $Date: 2012-03-29 12:01:22 -0600 (Thu, 29 Mar 2012) $
   By              :  $Author: jbrown $
   Rev             :  $Rev: 1244 $
"""

"""
TODO:
   Default copyright notice
"""

from django.conf.urls.defaults import patterns

from views import SSLProxyFetch


urlpatterns = patterns('',
    (r'^ssl/(?P<proto>http[s]?):/[/]?(?P<resource>[a-zA-Z0-9._/%\?]+)', SSLProxyFetch),
    # Some browsers may strip out that extra / after the proto, which is why
    # we parse the protocol and the resource separately
)


