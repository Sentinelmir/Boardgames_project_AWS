from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from games.views import HomePageView, GenreListView, GenreDetailView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomePageView.as_view(), name="home"),
    path("games/", include("games.urls")),
    path("genres/", GenreListView.as_view(), name="genre-list"),
    path("genres/<slug:genre>/", GenreDetailView.as_view(), name="genre-detail"),
    path("collections/", include("games_collections.urls")),
    path("reviews/", include("reviews.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)