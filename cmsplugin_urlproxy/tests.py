"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
import settings

class ProxyWhiteListTest(TestCase):
    fixtures=['southrockies.json']

    def setUp(self):
        self.old_squid = settings.USE_SQUID
        settings.USE_SQUID = False
        #TODO: coverage gap

    def tearDown(self):
        settings.USE_SQUID = self.old_squid


    def test_rejection(self):
        """
        Test that a non-allowed URL is rejected
        """
        c = Client()
        response = c.get('/ssl/http://www.evil.com')
        self.failUnlessEqual(response.status_code, 403)

    def test_acceptance(self):
        """
        Test that a permitted URL is sent
        """
        c = Client()
        response = c.get("/ssl/http://airquality.weather.gov/images/southrockies/smokes12_southrockies.png")
        self.failUnlessEqual(response.status_code, 200)

#class SimpleTest(TestCase):
#    def test_basic_addition(self):
#        """
#        Tests that 1 + 1 always equals 2.
#        """
#        self.failUnlessEqual(1 + 1, 2)
#
#__test__ = {"doctest": """
#Another way to test that 1 + 1 is equal to 2.
#
#>>> 1 + 1 == 2
#True
#"""}

