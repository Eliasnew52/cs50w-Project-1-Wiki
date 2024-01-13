from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:TITLE>", views.entry, name="entry"),
    path("search", views.search, name="search"),
     path("new_entry", views.new_entry, name="new_entry"),

]
