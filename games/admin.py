from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Game


@admin.register(Game)
class GameAdmin(ModelAdmin):
    list_display = ("title", "genres_display", "min_players", "max_players", "duration_min", "created_at")
    search_fields = ("title", "description")
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("created_at", "updated_at")

    @admin.display(description="Genres")
    def genres_display(self, obj):
        return obj.genres_display