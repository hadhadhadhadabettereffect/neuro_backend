from django.contrib import admin

from ordered_model.admin import OrderedModelAdmin

from .models import Product


class ProductAdmin(OrderedModelAdmin):
    list_display = ("name", "move_up_down_links")


admin.site.register(Product, ProductAdmin)
