import json
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.test import TestCase, Client
from mock import patch
from . import views
from .models import Subject


# checking that going to forum home page displays the list of subjects
class TestSubjectPage(TestCase):

    fixtures = ['subjects']

    def test_check_content_is_correct(self):
        subject_page = self.client.get('/forum/')
        self.assertTemplateUsed(subject_page, "forum/forum.html")
        subject_page_template_output = render_to_response("forum/forum.html",
                                                          {'subjects': Subject.objects.all()}).content
        self.assertEquals(subject_page.content, subject_page_template_output)


# checking that users can log in to post a new thread in forum page
class TestNewThreadAuthenticate(TestCase):

    def setUp(self):
        self.client = Client()
        self.url_path = '/forum/threads.html'
        self.data = {"email": "none@none.com", "password": "letmein1"}

    def test_api_authenticate_get(self):
        response = self.client.get(self.url_path)

        self.assertEqual(405, response.status_code)

    def test_api_authenticate_missing_fields(self):
        response = self.client.post(self.url_path, data=json.dumps({}))
        self.assertEqual(400, response.status_code)
        self.assertEqual(b'{"error": "Missing required field \'email\'"}', response.content)

    @patch('django.contrib.auth.authenticate')
    def test_api_authenticate_success(self, mock_authenticate):
        user = User()
        mock_authenticate.return_value = user
        response = self.client.post(self.url_path, data=json.dumps(self.data))
        self.assertContains(response, user.auth_token.key)


# check that users can see subjects in forum page
class TestForumPage(TestCase):

    def setUp(self):
        self.client = Client()

    def test_index_page(self):
        url = render_to_response('/forum/')
        response = self.client.post('/forum.html',{'subjects': Subject.objects.all()})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, '/forum/forum.html')
        self.assertContains(response, 'subjects')


# check that users can post subjects in a forum
class TestForum(TestCase):

    def test_forum(self):
        response = views.forum(self.request)
        self.assertContains(response, '/forum/forum.html',{'subjects': Subject.objects.all()})


# check that users can post threads in a forum
class TestThreads(TestCase):

    def test_threads(self):
        response = views.forum(self.request)
        self.assertContains(response, '/forum/threads.html',{'subjects': Subject.objects.all()})


# check that users can post threads in forum
class TestThread(TestCase):

    def setUp(self):
        self.client = Client()

    def test_thread_page(self):
        url = render_to_response('/forum/thread.html')
        response = self.client.post('/forum/thread.html',{'subjects': Subject.objects.all()})
        self.assertEqual(response.status_code, 200)
        self.assertNotEquals(response.status_code, 404)
        self.assertTemplateUsed(response, '/forum/thread.html')


