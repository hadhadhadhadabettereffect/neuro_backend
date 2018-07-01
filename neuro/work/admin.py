from django.contrib import admin

from ordered_model.admin import OrderedModelAdmin

from .models import Project, ProjectImage


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage

class ProjectAdmin(OrderedModelAdmin):
    list_display = ('name', 'move_up_down_links')
    inlines = [ ProjectImageInline ]


admin.site.register(Project, ProjectAdmin)