from django import forms
from .models import Mood


class MoodForm(forms.ModelForm):

    class Meta:
        model = Mood
        fields = ['name', 'icon']

        labels = {
            "name": "Mood Name",
            "icon": "Mood Icon"
        }

        help_texts = {
            "icon": "Use an emoji like 🌙 😴 💡 🌧️"
        }

        widgets = {
            "name": forms.TextInput(attrs={
                "placeholder": "Inspired, Calm, Anxious..."
            }),
            "icon": forms.TextInput(attrs={
                "placeholder": "🌙"
            })
        }
