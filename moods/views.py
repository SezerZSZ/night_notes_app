from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Mood
from .forms import MoodForm

# List all moods
class MoodListView(ListView):
    model = Mood
    template_name = "moods/mood-list.html"  # matches your template
    context_object_name = "moods"

# Create a new mood
class MoodCreateView(CreateView):
    model = Mood
    form_class = MoodForm
    template_name = "moods/mood-create.html"
    success_url = reverse_lazy("moods_list")  # redirects to list after creation

class MoodDeleteView(DeleteView):
    model = Mood
    template_name = "moods/mood-delete.html"
    success_url = reverse_lazy("moods_list")
