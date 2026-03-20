from django.db import models
from django.utils.text import slugify

from games.models import Game


class Collection(models.Model):
    title = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=140, unique=True, blank=True)
    description = models.TextField()

    banner = models.ImageField(
        upload_to="collections/",
        blank=True,
        null=True,
        help_text="Wide banner looks best.",
    )

    games = models.ManyToManyField(
        Game,
        related_name="collections",
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("title",)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title)
            self.slug = base or "collection"
        super().save(*args, **kwargs)