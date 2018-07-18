from django.http import JsonResponse

from .models import StoryPage


story_data = [
    page for page in StoryPage.objects.all().values()
]

def get_story_pages(request):
    return JsonResponse(story_data, safe=False)
