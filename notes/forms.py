from django import forms
from .models import Note


class NoteForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = ['title', 'content', 'category', 'moods', 'is_favorite',]

        labels = {
            "title": "Title of the note",
            "content": "Your Night Thought",
        }

        help_texts = {
            "title": "Give your thought a meaningful title.",
        }

        widgets = {
            "content": forms.Textarea(attrs={
                "placeholder": "Write your night reflection here...",
                "rows": 5
            }),
            "created_at": forms.DateTimeInput(attrs={
                "disabled": True
            })
        }

    def clean_title(self):
        title = self.cleaned_data.get("title")

        if len(title) < 3:
            raise forms.ValidationError(
                "Title must contain at least 3 characters."
            )

        return title

    def clean_content(self):
        content = self.cleaned_data.get("content")

        if len(content) < 10:
            raise forms.ValidationError(
                "Your thought must be at least 10 characters long."
            )

        return content
