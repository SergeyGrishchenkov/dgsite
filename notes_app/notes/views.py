from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<h4>Hello from Notes app.</h4>")



