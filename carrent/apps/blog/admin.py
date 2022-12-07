from django.contrib import admin
from .models import Blog, Tags, Category, Author, Paragraph


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')
    list_filter = ('category', 'tags')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')


class ParagraphAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')


admin.site.register(Blog, BlogAdmin)
admin.site.register(Tags)
admin.site.register(Category)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Paragraph, ParagraphAdmin)
