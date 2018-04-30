from django.contrib import admin

from neuro.singleton.admin import SingletonAdmin
from .models import Contact


class ContactAdmin(SingletonAdmin):
    list_display = ('header', 'email', 'message')
    list_display_links = ('header', 'email', 'message')

admin.site.register(Contact, ContactAdmin)