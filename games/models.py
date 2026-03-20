from django.contrib.postgres.fields import ArrayField
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Avg
from django.utils.text import slugify


class Game(models.Model):
    class Genre(models.TextChoices):
        ECONOMIC = "economic", "Economic"
        STRATEGY = "strategy", "Strategy"
        FAMILY = "family", "Family"
        PARTY = "party", "Party"
        COOPERATIVE = "cooperative", "Cooperative"
        ABSTRACT = "abstract", "Abstract"
        THEMATIC = "thematic", "Thematic"

    title = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=140, unique=True, blank=True)
    description = models.TextField()

    genres = ArrayField(
        base_field=models.CharField(max_length=20, choices=Genre.choices),
        default=list,
        blank=True,
    )

    min_players = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(20)]
    )
    max_players = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(20)]
    )
    duration_min = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(1000)]
    )
    age_min = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(99)],
        blank=True,
        null=True,
    )
    image = models.ImageField(upload_to="games/", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.title

    def clean(self):
        super().clean()
        errors = {}

        if self.min_players and self.max_players and self.min_players > self.max_players:
            errors["max_players"] = "Max players must be greater than or equal to min players."

        if not self.genres:
            errors["genres"] = "Select at least one genre."

        if errors:
            raise ValidationError(errors)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title) or "game"
        super().save(*args, **kwargs)

    @property
    def genre_pairs(self):
        choices_map = dict(self.Genre.choices)
        return [(value, choices_map.get(value, value)) for value in self.genres]

    @property
    def genres_display(self):
        return ", ".join(label for _, label in self.genre_pairs)

    @property
    def average_rating(self):
        avg = self.reviews.aggregate(avg_rating=Avg("rating"))["avg_rating"]
        return round(avg, 1) if avg is not None else None