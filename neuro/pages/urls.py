from django.urls import path
from . import views

urlpatterns = [
    # Notice the URL has been named
    path('', views.HomePageView.as_view(), name='home'),
    path('agency', views.get_agency_html, name='agency'),
    path('collection', views.get_collection_html, name='collection')
]
