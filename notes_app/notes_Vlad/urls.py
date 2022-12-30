from django.urls import path
from . import views

urlpatterns = [
    path('', views.NotesVlad.as_view(), name='NotesVlad'),
]
