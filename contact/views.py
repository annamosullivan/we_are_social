from contact.models import Feedback
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from .forms import ContactForm


def thanks(request):
    return render_to_response('/thanks.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            feedback = Feedback(subject=subject, sender=sender, email=email, message=message,)
            feedback.save()

            return HttpResponseRedirect(reverse('thanks'))
    else:
        form = ContactForm()

    return render_to_response('contact.html', {
        'form': form,
    }, context_instance=RequestContext(request))
