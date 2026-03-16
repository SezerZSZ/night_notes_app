from django.urls import path
from .views import CategoryListView, CategoryCreateView, CategoryDeleteView

urlpatterns = [
    path("", CategoryListView.as_view(), name="categories_list"),  # <-- must match base.html
    path("create/", CategoryCreateView.as_view(), name="category_create"),
    path("<int:pk>/delete/", CategoryDeleteView.as_view(), name="category_delete"),
]
