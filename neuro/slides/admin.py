from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from ordered_model.admin import OrderedModelAdmin

from .models import Image, Service, Work


class ImageInline(GenericTabularInline):
    model = Image


class ServiceAdmin(OrderedModelAdmin):
    list_display = ('name', 'move_up_down_links')


class WorkAdmin(OrderedModelAdmin):
    list_display = ('name', 'move_up_down_links')
    inlines = [ ImageInline ]


admin.site.register(Service, ServiceAdmin)
admin.site.register(Work, WorkAdmin)