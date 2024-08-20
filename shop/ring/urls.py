from django.urls import path

from . import views

urlpatterns = [
    #path("", views.index, name="index"),
    path("", views.main, name="start_page"),
    path("", views.sources, name="sources"),
    path("", views.main, name="start_page"),
    path("", views.main, name="start_page"),
    path("", views.main, name="start_page"),
    #path("sources", views.index, name="sources"),
]