from django.db import models
from datetime import datetime


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование категории')

    def __str__(self):
        return self.title


class NoteModel(models.Model):
    content = models.CharField(max_length=60, verbose_name='Заметка')
    text = models.TextField(null=True, blank=True, verbose_name='Текст заметки')
    reminder = models.DateTimeField(null=True, blank=True, verbose_name='Напоминание')
    time_add = models.DateTimeField(default=datetime.now, verbose_name='Время добавления заметки')

    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name='Категория')

    def __str__(self):
        return self.content
