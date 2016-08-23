from django.test import TestCase
import self as self
from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.core.urlresolvers import reverse, resolve
import unittest
import json
import mock
from mock import patch
from unittest import TestCase
from . import views
from threads.views import forum, threads, new_thread, thread, new_post, edit_post, delete_post, thread_vote, user_vote_button, vote_percentage
from .api_views import PostUpdateView, PostDeleteView
from .forms import ThreadForm, PostForm
from .serializers import PostSerializer
from .models import Subject, Thread, Post
from django.contrib.auth.models import AnonymousUser, User
from django.utils import timezone
from django.http import HttpResponse, Http404, HttpRequest
from rest_framework.request import Request
from templatetags.threads_extras import get_total_subject_posts, started_time, last_posted_user_name, user_vote_button, vote_percentage
from django.test import TestCase, RequestFactory, Client, TransactionTestCase


class SubjectPageTest(TestCase):

    fixtures = ['subjects']

    def test_check_content_is_correct(self):
        subject_page = self.client.get('/forum/')
        self.assertTemplateUsed(subject_page, "forum/forum.html")
        subject_page_template_output = render_to_response("forum/forum.html",
                                                          {'subjects': Subject.objects.all()}).content
        self.assertEquals(subject_page.content, subject_page_template_output)


class NewThreadAuthenticate(TestCase):

    def setUp(self):
        self.client = Client()
        self.url_path = '/forum/threads.html'
        self.data = {"email": "none@none.com", "password": "letmein1"}

    def test_api_authenticate_get(self):
        response = self.client.get(self.url_path)

        self.assertEqual(405, response.status_code)

    def test_api_authenticate_not_json(self):
        response = self.client.post(self.url_path, data='', content_type='application/json')

        self.assertEqual(400, response.status_code)
        self.assertEqual(b'{"error": "Could not parse body as JSON"}', response.content)

    def test_api_authenticate_missing_fields(self):
        response = self.client.post(self.url_path, data=json.dumps({}), content_type='application/json')

        self.assertEqual(400, response.status_code)
        self.assertEqual(b'{"error": "Missing required field \'email\'"}', response.content)

    def test_api_authenticate_failure(self):
        response = self.client.post(self.url_path, data=json.dumps(self.data), content_type='application/json')

        self.assertEqual(401, response.status_code)
        self.assertEqual(b'{"error": "Invalid credentials"}', response.content)

    @patch('django.contrib.auth.authenticate')
    def test_api_authenticate_success(self, mock_authenticate):
        user = User()
        mock_authenticate.return_value = user

        response = self.client.post(self.url_path, data=json.dumps(self.data), content_type='application/json')

        self.assertContains(response, user.auth_token.key)

class TestForumPage(TestCase):

    def setUp(self):
        self.client = Client()

    def test_index_page(self):
        url = render_to_response('/forum/')
        response = self.client.post('/forum.html',{'subjects': Subject.objects.all()})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, '/forum/forum.html')
        self.assertContains(response, 'subjects')



