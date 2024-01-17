from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:TITLE>", views.entry, name="entry"),
    path("random_page", views.Random_Entry, name="random_entry"),
    path("search", views.search, name="search"),
    path("new_entry", views.Entry_Creation, name="new_entry"),
    path("edit_page/<str:TITLE>", views.Entry_Edit, name="edit_page"),
]
