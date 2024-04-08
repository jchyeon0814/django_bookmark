from django.urls import path, include

from . import views

app_name = 'bookmark'

urlpatterns = [
    path("", views.BookmarkListView.as_view(), name="list"),
    path("add_page", views.AddView.as_view(), name="addPage"),
    path("add", views.add, name="add"),
]
