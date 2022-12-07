from django.contrib import admin
from .models import Contact
from .models import Subscribe


class AdminContact(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'is_solved')


admin.site.register(Contact, AdminContact)


admin.site.register(Subscribe)
