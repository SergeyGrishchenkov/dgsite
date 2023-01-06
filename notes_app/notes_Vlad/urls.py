from django.urls import path
from . import views

urlpatterns = [
    path('', views.NotesVlad.as_view(), name='NotesVlad'),
    path('delete_all/', views.delete_all, name='delete_all'),
]
