from django.contrib import admin
from .models import NoteModel, Category


@admin.register(Category)
class NoteFormAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(NoteModel)
class NoteFormAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'reminder', 'content', 'text']
    list_filter = ['category']
    search_fields = ['content']
