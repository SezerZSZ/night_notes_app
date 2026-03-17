from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Note, Category, Mood
from .models import Note
from .forms import NoteForm

# below are all the views that are neccessary, implemented

class NoteListView(ListView):
    model = Note
    template_name = "notes/notes-list.html"
    context_object_name = "notes"

    def get_queryset(self):
        queryset = super().get_queryset()
        title_query = self.request.GET.get("title", "")
        category_query = self.request.GET.get("category", "")
        mood_query = self.request.GET.get("mood", "")

        if title_query:
            queryset = queryset.filter(title__icontains=title_query)
        if category_query:
            queryset = queryset.filter(category__name__icontains=category_query)
        if mood_query:
            queryset = queryset.filter(moods__name__icontains=mood_query)

        return queryset.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["moods"] = Mood.objects.all()
        return context

class NoteDetailView(DetailView):
    model = Note
    template_name = "notes/note-details.html"
    context_object_name = "note"


class NoteCreateView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = "notes/note-create.html"
    success_url = reverse_lazy("notes_list")


class NoteUpdateView(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = "notes/note-edit.html"
    success_url = reverse_lazy("notes_list")


class NoteDeleteView(DeleteView):
    model = Note
    template_name = "notes/note-delete.html"
    success_url = reverse_lazy("notes_list")

class FavoriteNotesListView(ListView):
    model = Note
    template_name = "notes/favorite-notes.html"
    context_object_name = "notes"

    def get_queryset(self):
        # Only notes marked as favorite
        return Note.objects.filter(is_favorite=True)
