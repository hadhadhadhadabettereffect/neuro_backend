from django.contrib import admin

from .models import Services, AgencyService


class ServiceInline(admin.TabularInline):
    model = AgencyService


class ServicesAdmin(admin.ModelAdmin):
    inlines = [ServiceInline]


admin.site.register(Services, ServicesAdmin)
