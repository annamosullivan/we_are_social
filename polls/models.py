import datetime
from django.conf import settings
from django.db import models
from django.utils import timezone
from threads.models import Thread


class Poll(models.Model):

    question = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    thread = models.OneToOneField(Thread, null=True)
    pub_date = models.DateTimeField()

    def __unicode__(self):
        return self.question


class PollSubject(models.Model):

    name = models.CharField(max_length=255)
    poll = models.ForeignKey(Poll, related_name='subjects')

    def __unicode__(self):
        return self.name


class Vote(models.Model):

    poll = models.ForeignKey(Poll, related_name="votes")
    subject = models.ForeignKey(PollSubject, related_name="votes")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='votes')


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
