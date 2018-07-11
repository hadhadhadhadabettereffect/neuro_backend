from django.shortcuts import render
from django.views.generic import TemplateView

from neuro.products.models import Product
from neuro.work.models import Project

class HomePageView(TemplateView):
    template_name = "index.html"

def get_agency_html(request):
    return render(request, "agency.html", {
        'project_list': Project.objects.all()
    })

def get_collection_html(request):
    return render(request, "collection.html", {
        'product_list': Product.objects.all()
    })