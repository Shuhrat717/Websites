from django.contrib import admin
from .models import Team, Company, History


class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')


class HistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')


admin.site.register(History, HistoryAdmin)
admin.site.register(Team, TeamAdmin)

admin.site.register(Company, CompanyAdmin)
