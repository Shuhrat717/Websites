from django.contrib import admin

from .models import Contact


class AdminContact(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'created_at')


admin.site.register(Contact, AdminContact)