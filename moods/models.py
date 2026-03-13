from django.db import models

# Create your models here.

class Mood(models.Model):
    name = models.CharField(max_length=30, help_text="Enter a mood name")
    icon = models.CharField(max_length=5, help_text="Emoji representing the mood")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.icon} {self.name}"