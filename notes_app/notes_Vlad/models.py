from django.db import models


class NoteModel(models.Model):
    content = models.CharField(max_length=200, verbose_name='Заметка')
