from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Collection


@admin.register(Collection)
class CollectionAdmin(ModelAdmin):
    list_display = ("title", "slug", "created_at")
    search_fields = ("title", "description")
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("created_at",)
    filter_horizontal = ("games",)