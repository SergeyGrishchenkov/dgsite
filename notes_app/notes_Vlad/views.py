from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic import TemplateView


class NotesVlad(TemplateView):
    template_name = 'index_vlad.html'

    def get(self, request):
        ctx = {}
        return render(request, self.template_name, ctx)
