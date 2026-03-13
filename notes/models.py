from django.db import models
from categories.models import Category
from moods.models import Mood

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_favorite = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='notes')
    moods = models.ManyToManyField(Mood, blank=True, related_name='notes')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def word_count(self):
        return len(self.content.split())