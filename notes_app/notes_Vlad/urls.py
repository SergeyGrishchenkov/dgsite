from django.urls import path
from . import views

urlpatterns = [
    path('', views.notes_vlad, name='notes_Vlad'),
]
