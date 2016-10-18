from django import forms
from contact.models import Feedback


class ContactForm(forms.ModelForm):

    class Meta:
        model = Feedback
        exclude = []
