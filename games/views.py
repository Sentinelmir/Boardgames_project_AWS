from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, FormView

from games_collections.models import Collection
from .forms import GameCreateForm, GameEditForm, GameDeleteForm
from .models import Game


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_games"] = Game.objects.all()[:4]
        context["featured_collections"] = Collection.objects.prefetch_related("games")[:3]
        context["genre_choices"] = Game.Genre.choices
        return context

class GameListView(ListView):
    model = Game
    template_name = "games/game_list.html"
    context_object_name = "games"

    def get_queryset(self):
        queryset = Game.objects.all()

        genre = self.request.GET.get("genre")
        players = self.request.GET.get("players")
        sort = self.request.GET.get("sort")

        if genre in dict(Game.Genre.choices):
            queryset = queryset.filter(genres__overlap=[genre])

        if players and players.isdigit():
            players = int(players)
            queryset = queryset.filter(min_players__lte=players, max_players__gte=players)

        if sort == "title":
            queryset = queryset.order_by("title")
        elif sort == "duration":
            queryset = queryset.order_by("duration_min", "title")

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["genre_choices"] = Game.Genre.choices
        context["selected_genre"] = self.request.GET.get("genre", "")
        context["selected_players"] = self.request.GET.get("players", "")
        context["selected_sort"] = self.request.GET.get("sort", "")
        return context


class GameDetailView(DetailView):
    model = Game
    template_name = "games/game_detail.html"
    context_object_name = "game"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_queryset(self):
        return Game.objects.prefetch_related("reviews", "collections")


class GameCreateView(CreateView):
    model = Game
    form_class = GameCreateForm
    template_name = "games/game_form.html"

    def get_success_url(self):
        return reverse("games:detail", kwargs={"slug": self.object.slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Add game"
        context["submit_label"] = "Save game"
        context["cancel_url"] = reverse("games:list")
        return context


class GameUpdateView(UpdateView):
    model = Game
    form_class = GameEditForm
    template_name = "games/game_form.html"
    context_object_name = "game"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_success_url(self):
        return reverse("games:detail", kwargs={"slug": self.object.slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Edit game"
        context["submit_label"] = "Save changes"
        context["cancel_url"] = reverse("games:detail", kwargs={"slug": self.object.slug})
        return context


class GameDeleteView(FormView):
    template_name = "games/game_confirm_delete.html"
    form_class = GameDeleteForm
    success_url = reverse_lazy("games:list")

    def dispatch(self, request, *args, **kwargs):
        self.object = get_object_or_404(Game, slug=kwargs["slug"])
        return super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.object
        return kwargs

    def form_valid(self, form):
        form.save()
        return redirect("games:list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["game"] = self.object
        context["cancel_url"] = reverse("games:detail", kwargs={"slug": self.object.slug})
        return context


class GenreListView(TemplateView):
    template_name = "genres/genre_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        selected_genre = self.request.GET.get("genre", "")
        valid_genres = dict(Game.Genre.choices)

        genres = []
        for value, label in Game.Genre.choices:
            genres.append({
                "value": value,
                "label": label,
                "count": Game.objects.filter(genres__overlap=[value]).count(),
            })

        games = Game.objects.all()

        if selected_genre in valid_genres:
            games = games.filter(genres__overlap=[selected_genre])
            selected_genre_label = valid_genres[selected_genre]
        else:
            selected_genre = ""
            selected_genre_label = ""

        context["genres"] = genres
        context["games"] = games
        context["selected_genre"] = selected_genre
        context["selected_genre_label"] = selected_genre_label
        return context


class GenreDetailView(ListView):
    model = Game
    template_name = "genres/genre_detail.html"
    context_object_name = "games"

    def dispatch(self, request, *args, **kwargs):
        self.genre_value = kwargs["genre"]
        choices_map = dict(Game.Genre.choices)

        if self.genre_value not in choices_map:
            raise Http404("Genre does not exist.")

        self.genre_label = choices_map[self.genre_value]
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return Game.objects.filter(genres__overlap=[self.genre_value])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["genre_value"] = self.genre_value
        context["genre_label"] = self.genre_label
        return context