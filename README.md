django-cms-urlproxy
###################

When in the course of human events, it becomes necessary for one website to
dissolve the distinct networks that have separated them...

Why do you need a URL Proxy?
----------------------------

1. You have a mashup.
2. Your mashup is faster than the remote content source.
3. Your mashup is more available than the remote content source.
4. For some reason, your entire mashup is on HTTPS, and your users panic when
   they see a mixed content warning.  Also, some sites have SSL -- but their
   certificate is bad/expired.  This also generates client panicking warnings.

What this URL Proxy provides
----------------------------

1. An admin panel with white-listed URLs to the CMS, and a web proxy service.
2. An ad-hoc proxy service.  But I recommend you install SQUID instead.

Basically, it comes to this:
   /ssl/http://some.tiny.url will fetch and return whatever.

   As long as http://some.tiny.url is added to the accepted URL list.

   Note : If you are developing on the single threaded runserver, this will
   deadlock your test server until the proxied request fails if you test
   against a non-https image plugin (for example).


What is the author doing with this utility?
-------------------------------------------

Case #4 above.  We also do a lot of client side caching, but it was originally
written to proxy NOAA animated .gif images in an application that was provided
over SSL.

I think this is an awful idea
-----------------------------

I don't like proxying other place's content and re-presenting it signed by my
SSL certificate either.  But sometimes that's the lesser evil.

Yes, we're re-securing insecure content.  In the case of an <img src> there
isn't a lot of potential catastrophe here that would not happen if we inserted
the plain http anyway.

Squidutils.  Probably needs a better name.  Like "Insecure Proxy Bandaid"

TODO:
  - SSL Handling
    - I don't do certificate validation (and proxying SSL could be useful if you
      had a mashable with a self signed certificate)
    - I don't propagate certificate errors (how could I)
    - Even if I could do the above, it would be meaningless
    - Because we are pulling remote content in the page and then signing it.
  - Remove 'requirement' for squid.  This is really a SSL signing URL proxy.

To Use:
  1) Have Squid running locally
  2) Add app.plugins.squidutils to INSTALLED_APPS 
