from django.views.generic.edit import FormView
from .forms import FormNote
from django.http import HttpResponseRedirect
from .models import NoteModel, Category
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator


class SearchNotesView(View):
    template_name = 'index_vlad.html'

    def get(self, request):
        query = request.GET.get('q')
        notes = NoteModel.objects.filter(content__icontains=query)
        return render(request, self.template_name, {'notes': notes})


class DeleteAllView(View):
    def get(self, request):
        pass

    def post(self, request):
        NoteModel.objects.all().delete()
        messages.success(request, 'Все заметки были успешно удалены!')
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
            messages.error(request, 'Произошла ошибка при обновлении заметки. Пожалуйста, попробуйте еще раз.')
            return self.get(request, item_id)


class DeleteItemView(View):
    def get(self, request, item_id):
        item = NoteModel.objects.get(pk=item_id)
        item.delete()
        messages.success(request, 'Заметка была успешно удалена!')
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
        notes = NoteModel.objects.all().order_by('-id')
        category = self.request.GET.get('category')
        if category:
            notes = notes.filter(category__title=category)
        paginator = Paginator(notes, 3)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['notes'] = page_obj
        context['page_obj'] = page_obj
        context['categories'] = Category.objects.all()
        return context
