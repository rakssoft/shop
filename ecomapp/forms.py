from django.forms import ModelForm
from ecomapp.models import MailBox

class ContactForm(ModelForm):
    class Meta:
        model = MailBox
        fields = ['subject', 'sender', 'phone', 'message', 'copy']

class ContactFormCall(ModelForm):
    class Meta:
        model = MailBox
        fields = ['subject', 'phone', 'message', 'copy']