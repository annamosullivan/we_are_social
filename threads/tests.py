from django.test import TestCase
from django.shortcuts import render_to_response
from .models import Subject, Thread, Post
import difflib
import unittest
from unittest import TestCase
from django.test import Client
from . import views
from .api_views import PostUpdateView, PostDeleteView
from .forms import ThreadForm, PostForm
from .serializers import PostSerializer
from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory
from django.utils import timezone


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


class SubjectPageTest(TestCase):

    fixtures = ['subjects']
    def test_home_page_status_code_is_ok(self):
        home_page = self.client.get('/')
        self.assertEquals(home_page.status_code, 200)

    def test_check_content_is_correct(self):
        subject_page = self.client.get('/forum/')
        self.assertTemplateUsed(subject_page, "forum/forum.html")
        subject_page_template_output = render_to_response("forum/forum.html",
                                                          {'subjects':
        Subject.objects.all()}).content
        self.assertEquals(subject_page.content, subject_page_template_output)


class Threads(object):
    pass


class ThreadPageTest(TestCase):

    def test_home_page_status_code_is_ok(self):
        home_page = self.client.get('/')
        self.assertEquals(home_page.status_code, 200)

    def test_check_content_is_correct(self):
        threads_page = self.client.get('/forum/')
        self.assertTemplateUsed(threads_page, "forum/threads.html")
        threads_page_template_output = render_to_response("forum/forum.html",
                                                          {'threads':
        Threads.objects.all()}).content
        self.assertEquals(threads_page.content, threads_page_template_output)



