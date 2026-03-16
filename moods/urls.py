from django.urls import path
from .views import MoodListView, MoodCreateView

urlpatterns = [
    path("", MoodListView.as_view(), name="moods_list"),  # matches {% url 'moods_list' %}
    path("create/", MoodCreateView.as_view(), name="mood_create"),
]
