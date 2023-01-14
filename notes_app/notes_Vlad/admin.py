from django.contrib import admin
from .models import NoteModel, Category


@admin.register(Category)
@admin.register(NoteModel)
class NoteFormAdmin(admin.ModelAdmin):
    pass
