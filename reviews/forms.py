from django import forms
from .models import Review


class BaseReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["author_name", "rating", "text"]
        labels = {
            "author_name": "Your name",
            "rating": "Rating",
            "text": "Review text",
        }
        help_texts = {
            "text": "Write a short review with at least 10 characters.",
        }
        widgets = {
            "author_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Alex"}),
            "rating": forms.Select(
                attrs={"class": "form-select"},
                choices=[(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")],
            ),
            "text": forms.Textarea(attrs={"class": "form-control", "rows": 4, "placeholder": "What do you think about the game?"}),
        }

    def clean_author_name(self):
        author_name = self.cleaned_data["author_name"].strip()
        if len(author_name) < 2:
            raise forms.ValidationError("Your name must contain at least 2 characters.")
        return author_name

    def clean_text(self):
        text = self.cleaned_data["text"].strip()
        if len(text) < 10:
            raise forms.ValidationError("Review text must contain at least 10 characters.")
        return text


class ReviewCreateForm(BaseReviewForm):
    pass


class ReviewEditForm(BaseReviewForm):
    pass


class ReviewDeleteForm(BaseReviewForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.disabled = True

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance