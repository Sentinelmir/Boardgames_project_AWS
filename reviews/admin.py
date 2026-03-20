from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Review


@admin.register(Review)
class ReviewAdmin(ModelAdmin):
    list_display = ("game", "author_name", "rating", "created_at")
    list_filter = ("rating", "created_at")
    search_fields = ("game__title", "author_name", "text")
    readonly_fields = ("created_at",)