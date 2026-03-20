from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from games.models import Game


class Review(models.Model):
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        related_name="reviews",
    )

    author_name = models.CharField(max_length=60)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return f"{self.game.title} — {self.author_name} ({self.rating}/5)"