from django.forms import ModelForm
from .models import Contact


class FormContact(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'text']

    def __init__(self, *args, **kwargs):
        super(FormContact, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = "form-control"

