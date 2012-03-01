from django.contrib import admin
from .models import Menu

class MenuAdmin(admin.ModelAdmin):
    fields = ['label', 'url', 'sequence', 'visible']
    search_fields = ['label', 'url', 'visible']
    list_display = ['label', 'url', 'sequence', 'visible']

admin.site.register(Menu, MenuAdmin)

