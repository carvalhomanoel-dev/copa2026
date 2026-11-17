from django.urls import path 
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("brasil/", views.brasil, name="brasil"),
    path("marrocos/", views.marrocos, name="marrocos"),
]