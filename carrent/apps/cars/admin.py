from django.contrib import admin
from .models import Cars


class CarsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')


admin.site.register(Cars, CarsAdmin)