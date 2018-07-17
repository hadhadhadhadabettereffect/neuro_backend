from django.urls import path
from . import views

urlpatterns = [
    path('content.json', views.get_story_pages)
]
