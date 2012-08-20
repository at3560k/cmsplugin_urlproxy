from django.db import models


# REFACTORING of squid functionality from application
# into reusable plugin

class WhiteListedURLs(models.Model):
    """
    List of URLs that are permitted to be proxied by Django.  Why would you
    need a proxy in a web service or CMS you ask?  Because content is served
    over HTTPS.  And users panic and make bug reports when they get a mixed
    content warning.
    """
    allowed_url = models.URLField(
        max_length=500,
        blank=False,
        verbose_name = "CMS Secure URLs",
        help_text = "If you get a mixed content warning on a CMS page, you " \
        "should enter the URL here, and then edit the CMS URL to refer to " \
        "/ssl/SOME.example.com/some/page/1.jpg",
        unique = True # unique
    )

    class Meta:
        verbose_name = "White-Listed CMS URL"
        verbose_name_plural = "White-Listed CMS URLs"
        #app_label = 'cms'


