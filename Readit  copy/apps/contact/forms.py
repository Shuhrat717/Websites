from django.forms import ModelForm
from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'name',
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'email',
        })
        self.fields['subject'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'subject',
        })
        self.fields['message'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'message',
        })
