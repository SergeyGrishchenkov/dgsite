from django.contrib import admin
from .models import NoteForm


# Register your models here.

@admin.register(NoteForm)
class NoteFormAdmin(admin.ModelAdmin):
    pass
