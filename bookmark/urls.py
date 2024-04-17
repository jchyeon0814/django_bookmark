from django.urls import path, include
from .views import BookmarkListView, BookmarkCreateView, add

app_name = 'bookmark'

urlpatterns = [
    path("", BookmarkListView.as_view(), name="list"),
    path("add_page", BookmarkCreateView.as_view(), name="addPage"),
    path("add", add, name="add"),
]
