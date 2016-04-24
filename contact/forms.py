from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    sender = forms.EmailField(max_length=100)
    email = forms.EmailField(max_length=20)
    message = forms.CharField()
