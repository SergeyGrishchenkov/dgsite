from django.urls import path
from . import views

urlpatterns = [
    path('notes_Vlad/', views.say_hello, name='notes_Vlad'),
]
