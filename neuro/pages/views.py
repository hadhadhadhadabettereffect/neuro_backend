from itertools import chain
from operator import attrgetter
from django.shortcuts import render

from neuro.contact.models import Contact
from neuro.products.models import Product
from neuro.work.models import Project
from neuro.press.models import PressItem
from neuro.profiles.models import Profile
from neuro.story.models import StoryPage


context = {
    'agency_offsets_1': 1,
    'agency_offsets_2': 2,
    'agency_offsets_3': 3 + Project.objects.count(),
    'collection_offsets_1': 2,
    'collection_offsets_2': 3,
    'collection_offsets_3': 4,
    'press_list': PressItem.objects.all(),
    'product_list': Product.objects.all(),
    'profile_list': Profile.objects.all(),
    'project_list': Project.objects.all(),
    'storypage_list': StoryPage.objects.all(),
    'contact':  Contact.load().__dict__,
}


def get_home(request):
    return render(request, 'index.html', context)


def get_agency_html(request):
    return render(request, "agency.html", context)


def get_collection_html(request):
    return render(request, "collection.html", context)
