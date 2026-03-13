from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, help_text="Enter a unique category name")
    description = models.TextField(blank=True, help_text="Describe this category")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name