from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin

from .models import PressItem, PressImage, PressQuote


class PressItemAdmin(OrderedModelAdmin):
    list_display = ("name", "link", "move_up_down_links")

class PressImageAdmin(admin.ModelAdmin):
    pass

class PressQuoteAdmin(admin.ModelAdmin):
    pass

admin.site.register(PressImage, PressImageAdmin)
admin.site.register(PressQuote, PressQuoteAdmin)
admin.site.register(PressItem, PressItemAdmin)
