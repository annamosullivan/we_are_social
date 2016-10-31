import unittest
from django.contrib.auth.models import AnonymousUser, User
from django.contrib.auth import get_user_model
from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response
from django.test import RequestFactory
from django.test import TestCase
from home.views import get_index
from . import views


user = get_user_model()

# checking that users can access the template contact page
class SimpleTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='None', email='none@none.com', password='letmein1')


# check that user logs into a home page containing correct content and status code
class HomePageTest(TestCase):

    def test_home_page(self):
        home_page = resolve('/')
        self.assertEqual(home_page.func, get_index)

    def test_check_content_is_correct(self):
        home_page = resolve('/')
        # self.assertTemplateUsed(home_page, "index.html")
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
