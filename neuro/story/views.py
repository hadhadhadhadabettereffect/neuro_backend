from django.http import JsonResponse
from django.template.loader import render_to_string

from .models import StoryPage

stories = [
    render_to_string("story_page.html", page) for page in StoryPage.objects.all().values()
]


def get_story_pages(request):
    return JsonResponse(stories, safe=False)
