from unicodedata import category, name
from django.db import models

# Create your models here.

CHARS_MAX_LENGTH: int = 150

class Category(models. Model):
    """Category model class."""
    name = models.CharField(max_length=CHARS_MAX_LENGTH, blank=True)
    description = models.TextField(blank=True, null=True)


class Movie(models.Model):
    """Movie model class."""
    name = models.CharField(max_length=CHARS_MAX_LENGTH, blank=True)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    
class Tag(models.Models):
    """Tag model class."""
    name = models.CharField(max_length=CHARS_MAX_LENGTH, blank=True)
    description = models.TextField(blank=True, null=True)
        
