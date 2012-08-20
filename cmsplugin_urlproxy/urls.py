#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
urls.py

Pattern is /ssl/http://some.url
   or      /ssl/https://some.url
"""

from django.conf.urls.defaults import patterns

from views import SSLProxyFetch


urlpatterns = patterns('',
    (r'^ssl/(?P<proto>http[s]?):/[/]?(?P<resource>[a-zA-Z0-9._/%\?]+)', SSLProxyFetch),
    # Some browsers may strip out that extra / after the protocol, which is why
    # we parse the protocol and the resource separately
)


