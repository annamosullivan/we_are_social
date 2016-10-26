import datetime

from django.contrib.auth.models import AnonymousUser, User
from django.core import serializers
from django.core.urlresolvers import reverse
from django.test import TestCase, RequestFactory, Client
from django.utils import timezone
from . import views
from .models import Vote, Question


def create_question(question_text, days):
        """
        Creates a question with the given `question_text` and published the
        given number of `days` offset to now (negative for questions published
        in the past, positive for questions that have yet to be published).
        """
        time = timezone.now() + datetime.timedelta(days=days)
        return Question.objects.create(question_text=question_text, pub_date=time)


# checking to see if people can add past or future questions to a poll
class QuestionMethodTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertEqual(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=30)
        old_question = Question(pub_date=time)
        self.assertEqual(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() should return True for questions whose
        pub_date is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=1)
        recent_question = Question(pub_date=time)
        self.assertEqual(recent_question.was_published_recently(), True)


# checking to see if polls can be added with no questions,
# past or future questions in the list of questions


# checking to see if selecting invalid question types return appropriate status codes
class QuestionIndexDetailTests(TestCase):

    def test_detail_view_with_a_future_question(self):
        """
        The detail view of a question with a pub_date in the future should
        return a 404 not found.
        """
        future_question = create_question(question_text='Future question.', days=5)
        response = self.client.get(reverse('polls:detail', args=(future_question.id,)))
        self.assertEqual(response.status_code, 404)


# checking to see if valid votes, and invalid votes with missing polls/choices can be posted
class PollTest(TestCase):

    def test_ajax_vote(self):

        c = Client()

        # Extra parameters to make this a Ajax style request.
        kwargs = {'HTTP_X_REQUESTED_WITH':'XMLHttpRequest'}

        # A valid vote
        response = c.post('/polls/24/', {'choice': '1',}, **kwargs)
        # self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, '')

        # A invalid vote - choice doesn't exist
        response = c.post('/polls/1/vote/', {'choice': '10',}, **kwargs)
        self.assertEqual(response.status_code, 404)
        # self.assertEqual(response.content, '')

        # An invalid vote - poll doesn't exist
        response = c.post('/polls/2/vote/', {'choice': '1',}, **kwargs)
        self.assertEqual(response.status_code, 404)


