from django.views.generic.edit import FormView
from .forms import FormNote
from django.http import HttpResponseRedirect
from .models import NoteModel
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView


class NotesListView(ListView):
    model = NoteModel
    paginate_by = 3


class DeleteAllView(View):
    def get(self, request):
        pass

    def post(self, request):
        NoteModel.objects.all().delete()
        return HttpResponseRedirect(reverse('NotesVlad'))


class UpdateItemView(View):
    def get(self, request, item_id):
        my_model = NoteModel.objects.get(pk=item_id)
        form = FormNote(instance=my_model)
        notes = NoteModel.objects.all()
        ctx = {'form': form, 'notes': notes}
        return render(request, 'index_vlad.html', ctx)

    def post(self, request, item_id):
        my_model = NoteModel.objects.get(pk=item_id)
        form = FormNote(request.POST, instance=my_model)
        if form.is_valid():
            form.save()
            messages.success(request, 'Заметка успешно сохранена!')
            return HttpResponseRedirect(reverse('NotesVlad'))
        else:
            return self.get(request, item_id)


class DeleteItemView(View):
    def get(self, request, item_id):
        item = NoteModel.objects.get(pk=item_id)
        item.delete()
        return HttpResponseRedirect(reverse('NotesVlad'))


class NotesVlad(FormView):
    template_name = 'index_vlad.html'
    form_class = FormNote
    success_url = reverse_lazy('NotesVlad')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Заметка успешно сохранена!')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes'] = NoteModel.objects.all()
        return context
