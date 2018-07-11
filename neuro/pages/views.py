from django.shortcuts import render
from django.views.generic import TemplateView

from neuro.products.models import Product


class HomePageView(TemplateView):
    template_name = "index.html"

def get_collection_html(request):
    return render(request, "collection.html", {
        'product_list': Product.objects.all()
    })