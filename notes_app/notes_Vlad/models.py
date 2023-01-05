from django.db import models


class NoteForm(models.Model):
    objects = None
    content = models.CharField(max_length=200)
