from django.contrib import admin

from .models import Comments


@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'created_at')
    date_hierarchy = 'created_at'
    search_fields = ('name', 'email')
    search_help_text = 'hello'


