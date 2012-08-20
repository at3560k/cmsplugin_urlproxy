from django.db import models
from django.utils.translation import ugettext_lazy as _

from cmsplugin_urlproxy.util import sessionlessProxyFetch

class WhiteListedURLs(models.Model):
    """
    List of URLs that are permitted to be proxied by Django.  Why would you
    need a proxy in a web service or CMS you ask?  Because content is served
    over HTTPS.  And users panic and make bug reports when they get a mixed
    content warning.
    """

    # Length not a constant because that would change DB Schema
    allowed_url = models.URLField(
        max_length=500,
        blank=False,
        verbose_name = "Authorized Proxy URLs",
        help_text = _("If you get a mixed content warning on a CMS page, " + \
        "you should enter the URL here, and then edit the CMS URL to " + \
        "refer to /ssl/SOME.example.com/some/page/1.jpg"),
        unique = True # unique
    )

    class Meta:
        verbose_name = _("White-Listed CMS URL")
        verbose_name_plural = _("White-Listed CMS URLs")
        #app_label = 'cms'

    def fetch(self):
        return sessionlessProxyFetch(self.allowed_url)

