from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Note
from .forms import NoteForm

# below are all the views that are neccessary, implemented

class NoteListView(ListView):
    model = Note
    template_name = "notes/notes-list.html"
    context_object_name = "notes"

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
