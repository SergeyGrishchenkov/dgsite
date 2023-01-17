from django.contrib import admin
from django.urls import path

from notes.views import index

urlpatterns = [
    path('', index, name="main_notes"),
]
