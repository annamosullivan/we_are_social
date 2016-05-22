from django.test import TestCase
from .models import Membership
import paypal.standard.forms
from paypal.standard.forms import PayPalPaymentsForm
from django import forms
from django.conf import settings
from django.db import models
import unittest
from django.test import Client
from . import views
from admin import BookAdmin
from models import Membership
from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory


class SimpleTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='None', email='none@none.com', password='letmein1')

    def test_details(self):
        # Create an instance of a GET request.
        request = self.factory.get('/accounts/login')

        # Recall that middleware are not supported. You can simulate a
        # logged-in user by setting request.user manually.
        request.user = self.user

        # Or you can simulate an anonymous user by setting request.user to
        # an AnonymousUser instance.
        request.user = AnonymousUser()

        # Test my_view() as if it were deployed at /customer/details
        response = views(request)
        # Use this syntax for class-based views.
        response = views.as_view()(request)
        self.assertEqual(response.status_code, 200)









