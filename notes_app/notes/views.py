from django.http import HttpResponse
from django.shortcuts import render

def index1(request):
    # return HttpResponse("<h4>Hello from Notes app.</h4>")
    return render(request, 'index1.html')

def index2(request):
    # return HttpResponse("<h4>Hello from Notes app.</h4>")
    return render(request, 'index.html')


