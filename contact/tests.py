from django.test import TestCase
from django.db import models
from .forms import ContactForm
from .models import Feedback
from django import forms
from django.conf import settings
import unittest
from django.test import Client
from . import views
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

        # Create an instance of a POST request.
        request = self.factory.post('/accounts/login')

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


class CustomContactTest(TestCase):

    def test_manager_create(self, Contact=None):
        contact = Contact._create_contact(None, "Joe Bloggs", "test@test.com", "message")
        self.assertIsNotNone(contact)

        with self.assertRaises(ValueError):
            contact = Contact._create_contact(None, "Joe Bloggs", "test@test.com", "message")

    def test_contact_form(self):
        form = ContactForm({
            'subject': "aaaa",
            'sender': "Joe Bloggs",
            'email': 'test@test.com',
            'message': "xxxx"
        })

        self.assertTrue(form.is_valid())

    def test_contact_form_fails_with_missing_subject(self):
        form = ContactForm({
            'subject': "aaaa",
            'sender': "Joe Bloggs",
            'email': 'test@test.com',
            'message': "xxxx"
        })

        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Please enter a subject",
                                 form.full_clean())

    def test_contact_form_fails_with_missing_sender(self):
        form = ContactForm({
            'subject': "aaaa",
            'sender': "Joe Bloggs",
            'email': 'test@test.com',
            'message': "xxxx"
        })

        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Please enter your name",
                                 form.full_clean())

    def test_contact_form_fails_with_missing_email(self):
        form = ContactForm({
            'subject': "aaaa",
            'sender': "Joe Bloggs",
            'email': 'test@test.com',
            'message': "xxxx"
        })

        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Please enter your email address",
                                 form.full_clean())

    def test_contact_form_fails_with_missing_message(self):
        form = ContactForm({
            'subject': "aaaa",
            'sender': "Joe Bloggs",
            'email': 'test@test.com',
            'message': "xxxx"
        })

        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Please enter a message",
                                 form.full_clean())

    def test_contact_form_fails_with_emails_that_are_invalid(self):
        form = ContactForm({
            'subject': "aaaa",
            'sender': "Joe Bloggs",
            'email': 'test@test.com',
            'message': "xxxx"
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Invalid e-mail.Please enter in format joe@bloggs.com",
                                 form.full_clean())

