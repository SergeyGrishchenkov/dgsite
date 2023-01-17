from crispy_forms.bootstrap import PrependedText, FormActions
from django import forms
from django.urls import reverse_lazy

from .models import NoteModel
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset
from crispy_forms.layout import Row, Column


class FormNote(forms.ModelForm):
    reminder = forms.DateTimeField(widget=forms.TextInput(attrs={'type': 'datetime-local'}), label='Напоминание',
                                   required=False)

    class Meta:
        model = NoteModel
        fields = ['category', 'reminder', 'content', 'text']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('NotesVlad')
        self.helper.form_method = 'get'
        self.helper.layout = Layout(
            Row(
                Column('category', css_class='form-group col-md-6'),
                Column('reminder', css_class='form-group col-md-6'),
                css_class='form-row'
            ),
            Row(
                Column('@', 'content', css_class='form-group col-md-12'),
                css_class='form-row'
            ),
            'text',
            FormActions(
                Submit('submit', 'Save'),
            )
        )
