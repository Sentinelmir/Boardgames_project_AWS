from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, FormView

from games.models import Game
from .forms import ReviewCreateForm, ReviewEditForm, ReviewDeleteForm
from .models import Review


class ReviewListView(ListView):
    model = Review
    template_name = "reviews/review_list.html"
    context_object_name = "reviews"

    def get_queryset(self):
        queryset = Review.objects.select_related("game")
        self.current_game = None

        game_slug = self.request.GET.get("game")
        if game_slug:
            self.current_game = get_object_or_404(Game, slug=game_slug)
            queryset = queryset.filter(game=self.current_game)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_game"] = self.current_game
        return context


class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewCreateForm
    template_name = "reviews/review_form.html"

    def dispatch(self, request, *args, **kwargs):
        self.game = get_object_or_404(Game, slug=kwargs["game_slug"])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.game = self.game
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("games:detail", kwargs={"slug": self.game.slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["game"] = self.game
        context["page_title"] = "Add review"
        context["submit_label"] = "Save review"
        context["cancel_url"] = reverse("games:detail", kwargs={"slug": self.game.slug})
        return context


class ReviewUpdateView(UpdateView):
    model = Review
    form_class = ReviewEditForm
    template_name = "reviews/review_form.html"
    context_object_name = "review"

    def get_queryset(self):
        return Review.objects.select_related("game")

    def get_success_url(self):
        return reverse("games:detail", kwargs={"slug": self.object.game.slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["game"] = self.object.game
        context["page_title"] = "Edit review"
        context["submit_label"] = "Save changes"
        context["cancel_url"] = reverse("games:detail", kwargs={"slug": self.object.game.slug})
        return context


class ReviewDeleteView(FormView):
    template_name = "reviews/review_confirm_delete.html"
    form_class = ReviewDeleteForm

    def dispatch(self, request, *args, **kwargs):
        self.object = get_object_or_404(Review.objects.select_related("game"), pk=kwargs["pk"])
        return super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.object
        return kwargs

    def form_valid(self, form):
        game_slug = self.object.game.slug
        form.save()
        return redirect("games:detail", slug=game_slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["review"] = self.object
        context["game"] = self.object.game
        context["cancel_url"] = reverse("games:detail", kwargs={"slug": self.object.game.slug})
        return context