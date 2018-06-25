from django.contrib import admin

from .models import PressImage, PressQuote


class PressImageAdmin(admin.ModelAdmin):
    pass

class PressQuoteAdmin(admin.ModelAdmin):
    pass

admin.site.register(PressImage, PressImageAdmin)
admin.site.register(PressQuote, PressQuoteAdmin)
