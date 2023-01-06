from django.views.generic import TemplateView
from .forms import FormNote
from django.http import HttpResponseRedirect
from .models import NoteForm
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import render
import tkinter as tk


def delete_all(request):
    NoteForm.objects.all().delete()
    return HttpResponseRedirect(reverse('NotesVlad'))


class NotesVlad(TemplateView):
    template_name = 'index_vlad.html'

    def get(self, request, *args, **kwargs):
        form = FormNote()
        notes = NoteForm.objects.all()
        ctx = {'form': form, 'notes': notes}
        return render(request, self.template_name, ctx)

    def post(self, request):
        form = FormNote(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Заметка успешно сохранена!')  # пока не отображается
            return HttpResponseRedirect(reverse('NotesVlad'))
        notes = NoteForm.objects.all()
        ctx = {'form': form, 'notes': notes}
        return render(request, self.template_name, ctx)
