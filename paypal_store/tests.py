import unittest
from . import views
from django.shortcuts import render_to_response
from django.test import Client
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic


class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_paypal_cancel(self):
        # Issue a GET request.
        response = self.client.get('/paypal/paypal_cancel.html/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

    def test_paypal_return(self):
        # Issue a GET request.
        response = self.client.get('/paypal/paypal_return.html/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)


def test_home_page_status_code_is_ok(self):
    home_page = self.client.get('/')
    self.assertEquals(home_page.status_code, 200)


def test_check_paypal_return_is_correct(self):
        home_page = self.client.get('/')
        self.assertTemplateUsed(home_page, 'paypal/paypal_return.html')
        home_page_template_output = render_to_response('paypal/paypal_return.html').content
        self.assertEquals(home_page.content, home_page_template_output)


def test_check_paypal_cancel_is_correct(self):
        home_page = self.client.get('/')
        self.assertTemplateUsed(home_page, 'paypal/paypal_cancel.html')
        home_page_template_output = render_to_response('paypal/paypal_cancel.html').content
        self.assertEquals(home_page.content, home_page_template_output)


