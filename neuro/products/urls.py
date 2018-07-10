from django.urls import path

from . import views

urlpatterns = [
    path('data.json', views.product_data),
]
