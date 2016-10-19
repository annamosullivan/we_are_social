from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from .forms import ContactForm
from django.core.mail import send_mail
from email.utils import formataddr
from django.conf import settings


def send_email(subject, message, email, name):
    send_mail(
        subject,
        message,
        settings.REPLY_TO,
        [formataddr((name, email))],
        fail_silently=False,
    )


def thanks(request):
    return render_to_response('thanks.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_data = form.save()
            send_email(contact_data.subject, contact_data.message, contact_data.email, contact_data.name)
            return HttpResponseRedirect(reverse('thanks'))
    else:
        form = ContactForm()

    return render_to_response('contact.html', {
        'form': form,
    }, context_instance=RequestContext(request))
