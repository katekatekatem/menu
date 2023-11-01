from django.contrib import admin

from .models import Menu


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'url', 'parent')
    list_filter = ('name',)
    search_fields = ('name', 'url')
