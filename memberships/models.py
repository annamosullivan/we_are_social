import uuid
from django import template
import paypal.standard.forms
from django.conf import settings
from django.db import models
from paypal.standard.forms import PayPalPaymentsForm


class Membership(models.Model):

    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    @property
    def paypal_form(self):
        paypal_dict = {
            "business": settings.PAYPAL_RECEIVER_EMAIL,
            "amount": self.price,
            "currency": "USD",
            "cmd": "_xclick-subscriptions",
            "invoice": uuid.uuid4,
            "item_name": "%s-%s" % (self.name, uuid.uuid4()),
            "notify_url": settings.PAYPAL_NOTIFY_URL,
            "return_url": "%s/paypal-return/" % settings.SITE_URL,
            "cancel_return": "%s/paypal-cancel/" % settings.SITE_URL
        }

        return paypal.standard.forms.PayPalPaymentsForm(initial=paypal_dict)

    # render the form
        if settings.DEBUG:
            html = PayPalPaymentsForm(initial=paypal_dict,button_type='subscribe').render()
        else:
            html = PayPalPaymentsForm(initial=paypal_dict,button_type='subscribe').render()
        return html

