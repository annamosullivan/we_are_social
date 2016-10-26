import json
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.test import TestCase, Client
from mock import patch
from . import views
from .models import Subject
import difflib


# checking that going to forum home page displays the list of subjects
class TestSubjectPage(TestCase):

    fixtures = ['subjects']

    def test_check_content_is_correct(self):
        subject_page = self.client.get('templates/forum/')
        # subject_page_template_output = render_to_response("forum/forum.html", {'subjects': Subject.objects.all()}).content
        self.assertEquals(subject_page.content, subject_page_template_output)


# checking that users can log in to post a new thread in forum page
class TestNewThreadAuthenticate(TestCase):

    def setUp(self):
        self.client = Client()
        self.url_path = '/forum/threads.html'
        self.data = {"email": "none@none.com", "password": "letmein1"}

    def test_api_authenticate_get(self):
        response = self.client.get(self.url_path)

        self.assertEqual(404, response.status_code)


# check that users can see subjects in forum page
class TestForumPage(TestCase):

    def setUp(self):
        self.client = Client()


# check that users can post threads in forum
class TestThread(TestCase):

    def setUp(self):
        self.client = Client()



