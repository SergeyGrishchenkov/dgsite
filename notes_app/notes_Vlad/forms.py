from django import forms
from .models import NoteForm


class FormNote(forms.ModelForm):
    class Meta:
        model = NoteForm
        fields = ['content']
