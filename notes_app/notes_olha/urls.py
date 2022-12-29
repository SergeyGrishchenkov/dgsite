from django.urls import path
from . import views
urlpatterns = [
    path('hello_from_Olha/', views.hello, name='hello')
]