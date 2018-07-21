from itertools import chain
from operator import attrgetter
from django.shortcuts import render

from neuro.contact.models import Contact
from neuro.products.models import Product
from neuro.work.models import Project
from neuro.press.models import PressItem
from neuro.profiles.models import Profile
from neuro.story.models import StoryPage

agency_offsets = [0,1,2,2 + Project.objects.count()]
collection_offsets = [0,2,3,4]
agency_video = ""
collection_video = "static/Neuro-Campaign"
home_video = "static/Neuro-Homepage"
story_page_types = [ p.page_type for p in StoryPage.objects.all() ]

context = {
    'agency_offsets_1': agency_offsets[1],
    'agency_offsets_2': agency_offsets[2],
    'agency_offsets_3': agency_offsets[3],
    'collection_offsets_1': collection_offsets[1],
    'collection_offsets_2': collection_offsets[2],
    'collection_offsets_3': collection_offsets[3],
    'press_list': PressItem.objects.all(),
    'product_list': Product.objects.all(),
    'profile_list': Profile.objects.all(),
    'project_list': Project.objects.all(),
    'storypage_list': StoryPage.objects.all(),
    'contact':  Contact.load().__dict__,
    'agency_video': agency_video,
    'collection_video': collection_video,
    'home_video': home_video,
    'json_data': {
        'active': 2,
        'offsets': [
            agency_offsets,
            collection_offsets
        ],
        'videos': [
            agency_video,
            collection_video,
            home_video
        ],
        'story_page_types': story_page_types
    }
}


def get_home(request):
    return render(request, 'index.html', context)


def get_agency_html(request):
    ctx = context.copy()
    ctx["json_data"]["active"] = 0
    return render(request, "index.html", ctx)


def get_collection_html(request):
    ctx = context.copy()
    ctx["json_data"]["active"] = 1
    return render(request, "index.html", ctx)

