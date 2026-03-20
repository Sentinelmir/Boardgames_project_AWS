from django.urls import path
from .views import CollectionListView, CollectionDetailView

app_name = "collections"

urlpatterns = [
    path("", CollectionListView.as_view(), name="list"),
    path("<slug:slug>/", CollectionDetailView.as_view(), name="detail"),
]