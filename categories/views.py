from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView
from .models import Category
from .forms import CategoryForm
from django.urls import reverse_lazy

class CategoryListView(ListView):
    model = Category
    template_name = "categories/category-list.html"
    context_object_name = "categories"

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "categories/category-create.html"
    success_url = reverse_lazy("categories_list")

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = "categories/category-delete.html"
    success_url = reverse_lazy("categories_list")

