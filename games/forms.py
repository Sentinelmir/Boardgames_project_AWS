from django import forms
from .models import Game


class BaseGameForm(forms.ModelForm):
    genres = forms.MultipleChoiceField(
        choices=Game.Genre.choices,
        widget=forms.SelectMultiple(attrs={"class": "form-select", "size": 7}),
        label="Genres",
        help_text="Hold Ctrl/Cmd to select multiple genres.",
        error_messages={"required": "Select at least one genre."},
    )

    class Meta:
        model = Game
        fields = [
            "title",
            "description",
            "genres",
            "min_players",
            "max_players",
            "duration_min",
            "age_min",
            "image",
        ]
        labels = {
            "title": "Game title",
            "description": "Description",
            "min_players": "Min players",
            "max_players": "Max players",
            "duration_min": "Duration in minutes",
            "age_min": "Minimum age",
            "image": "Cover image",
        }
        help_texts = {
            "description": "Write a short but meaningful description.",
            "age_min": "Optional field.",
            "image": "Optional field.",
        }
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Brass: Birmingham"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4, "placeholder": "Describe the game..."}),
            "min_players": forms.NumberInput(attrs={"class": "form-control", "placeholder": "2"}),
            "max_players": forms.NumberInput(attrs={"class": "form-control", "placeholder": "4"}),
            "duration_min": forms.NumberInput(attrs={"class": "form-control", "placeholder": "120"}),
            "age_min": forms.NumberInput(attrs={"class": "form-control", "placeholder": "14"}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }

    def clean_title(self):
        title = self.cleaned_data["title"].strip()
        if len(title) < 2:
            raise forms.ValidationError("Title must contain at least 2 characters.")
        return title

    def clean_description(self):
        description = self.cleaned_data["description"].strip()
        if len(description) < 20:
            raise forms.ValidationError("Description must contain at least 20 characters.")
        return description

    def clean(self):
        cleaned_data = super().clean()
        min_players = cleaned_data.get("min_players")
        max_players = cleaned_data.get("max_players")

        if min_players and max_players and min_players > max_players:
            self.add_error("max_players", "Max players must be greater than or equal to min players.")

        return cleaned_data


class GameCreateForm(BaseGameForm):
    pass


class GameEditForm(BaseGameForm):
    pass


class GameDeleteForm(BaseGameForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.disabled = True

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance