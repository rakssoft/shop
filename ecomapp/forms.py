from django.forms import ModelForm
from ecomapp.models import MailBox

class ContactForm(ModelForm):
    class Meta:
        model = MailBox
        fields = ['subject', 'sender', 'phone', 'message', 'copy']