from django.db import models


class Feedback(models.Model):
    subject = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __unicode__(self):
        return "Subject:{subject}\nSender:{sender}\n{msg}".format(subject=self.subject, sender=self.sender, email=self.email, msg=self.message)