from django.shortcuts import render

from neuro.contact.models import Contact
from neuro.products.models import Product
from neuro.work.models import Project


context = {
    'agency_offsets_1': 1,
    'agency_offsets_2': 2,
    'agency_offsets_3': 2 + Project.objects.count(),
    'collection_offsets_1': 2,
    'collection_offsets_2': 3,
    'collection_offsets_3': 4,
    'product_list': Product.objects.all(),
    'project_list': Project.objects.all(),
    'contact':  Contact.load().__dict__,
}


def get_home(request):
    a_offsets = [0, 1, 2, 2 + Project.objects.count()]

    return render(request, 'index.html', context)


def get_agency_html(request):
    return render(request, "agency.html", context)


def get_collection_html(request):
    return render(request, "collection.html", context)
