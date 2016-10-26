import unittest
from django.contrib.auth.models import AnonymousUser, User
from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response
from django.test import RequestFactory
from django.test import TestCase
from home.views import get_index
from . import views

# check that user logs into a home page containing correct content and status code
class HomePageTest(TestCase):

    def test_home_page(self):
        home_page = resolve('/')
        self.assertEqual(home_page.func, get_index)

    def test_check_content_is_correct(self):
        home_page = resolve('/')
        self.assertTemplateUsed(home_page, "index.html")
        home_page_template_output = render_to_response("index.html", {'user': self.user}).content
        self.assertEquals(home_page.content, home_page_template_output)


class TestHomeConfig(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_home_config(self):
        self.failUnless('home')

    def main(self):
        unittest.main()

    if __name__ == '__main__':
        main()
