from django.urls import path
from . import views

urlpatterns = [
    path('', views.NotesVlad.as_view(), name='NotesVlad'),
    path('delete_all/', views.delete_all, name='delete_all'),
    path('delete_item/<int:item_id>/', views.delete_item, name='delete_item'),
    path('update_item/<int:item_id>/', views.update_item, name='update_item'),
]
