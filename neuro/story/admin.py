from django.contrib import admin

from ordered_model.admin import OrderedModelAdmin

from .models import StoryPage


class StoryAdmin(OrderedModelAdmin):
    list_display = ('title', 'move_up_down_links')

admin.site.register(StoryPage, StoryAdmin)
