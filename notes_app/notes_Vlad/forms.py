from django import forms
from .models import NoteModel


class FormNote(forms.ModelForm):
    class Meta:
        model = NoteModel
        fields = ['category', 'reminder', 'content', 'text']
