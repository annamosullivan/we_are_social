import unittest
from unittest import TestCase
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.test import Client


# check that users are redirected to paypal home page after completing a transaction
# check that users are redirected to paypal cancel page after cancelling a transaction
class SimpleTest(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()





