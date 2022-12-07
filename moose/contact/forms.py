from django.forms import ModelForm
from .models import Contact
from .models import Subscribe


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = "form-control"


class Subscribe(ModelForm):
    class Meta:
        model = Contact
        fields = ['email']

    def __init__(self, *args, **kwargs):
        super(Subscribe, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = "form-control"

