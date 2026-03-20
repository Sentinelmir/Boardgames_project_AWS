from django.views.generic import ListView, DetailView
from .models import Collection


class CollectionListView(ListView):
    model = Collection
    template_name = "collections/collection_list.html"
    context_object_name = "collections"

    def get_queryset(self):
        return Collection.objects.prefetch_related("games")


class CollectionDetailView(DetailView):
    model = Collection
    template_name = "collections/collection_detail.html"
    context_object_name = "collection"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_queryset(self):
        return Collection.objects.prefetch_related("games")