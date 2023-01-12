from django import forms
from .models import NoteModel


class FormNote(forms.ModelForm):
    reminder = forms.DateTimeField(widget=forms.TextInput(attrs={'type': 'datetime-local'}), label='Напоминание',
                                   required=False)

    class Meta:
        model = NoteModel
        fields = ['category', 'reminder', 'content', 'text']
