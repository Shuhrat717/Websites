from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'created_at', 'is_published')


admin.site.register(Contact, ContactAdmin)
