from django.urls import path, include
from .views import BookmarkListView, BookmarkCreateView, BookmarkDetailView, BookmarkModifyView

app_name = 'bookmark'

urlpatterns = [
    path("", BookmarkListView.as_view(), name="list"),
    path("add/", BookmarkCreateView.as_view(), name="add"),
    path("detail/<int:pk>/", BookmarkDetailView.as_view(), name="detail"),
    path("modify/<int:pk>/", BookmarkModifyView.as_view(), name="modify"),
]
