from django.test import TestCase
from django.db import models
from .forms import ContactForm
from django import forms
from django.conf import settings


class CustomContactTest(TestCase):

    def test_manager_create(self, Contact=None):
        contact = Contact.objects._create_contact(None, "Joe Bloggs", "test@test.com", "message")
        self.assertIsNotNone(contact)

        with self.assertRaises(ValueError):
            contact = Contact.objects._create_contact(None, "Joe Bloggs", "test@test.com", "message")

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

