from django.contrib import admin
from django.urls import path

from notes.views import index2

urlpatterns = [
    path('', index2, name="main_notes"),
]
