from django.urls import path
from neuro.pages import views

urlpatterns = [
    # Notice the URL has been named
    path('', views.HomePageView.as_view(), name='home'),
]
