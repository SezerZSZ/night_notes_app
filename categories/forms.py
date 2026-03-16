from django import forms
from .models import Category


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['name', 'description']

        labels = {
            "name": "Category Name",
            "description": "Category Description"
        }

        help_texts = {
            "name": "Example: Dreams, Ideas, Reflections"
        }

        widgets = {
            "description": forms.Textarea(attrs={
                "placeholder": "Describe what this category represents...",
                "rows": 3
            })
        }

    def clean_name(self):
        name = self.cleaned_data.get("name")

        if Category.objects.filter(name__iexact=name).exists():
            raise forms.ValidationError(
                "This category already exists. Try another name"
            )

        return name
