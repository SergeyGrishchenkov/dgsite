from django.contrib import admin
from django.urls import path

from notes_sergey.views import index1

urlpatterns = [
    path('', index1, name="index"),
]
