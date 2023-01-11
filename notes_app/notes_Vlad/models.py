from django.db import models
from datetime import datetime


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class NoteModel(models.Model):
    content = models.CharField(max_length=100)
    text = models.TextField(null=True, blank=True)
    reminder = models.DateTimeField(null=True, blank=True)
    time_add = models.DateTimeField(default=datetime.now)

    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True, blank=True)
