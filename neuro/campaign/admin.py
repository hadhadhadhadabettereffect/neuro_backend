from django.contrib import admin

from .models import Campaign, CampaignImage


class CampaignImageInline(admin.TabularInline):
    model = CampaignImage

class CampaignAdmin(admin.ModelAdmin):
    inlines = [CampaignImageInline]

admin.site.register(Campaign, CampaignAdmin)
