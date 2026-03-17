from django.urls import path
from .views import MoodListView, MoodCreateView, MoodDeleteView

urlpatterns = [
    path("", MoodListView.as_view(), name="moods_list"),  # matches {% url 'moods_list' %}
    path("create/", MoodCreateView.as_view(), name="mood_create"),
    path("<int:pk>/delete/", MoodDeleteView.as_view(), name="mood_delete"),
]
