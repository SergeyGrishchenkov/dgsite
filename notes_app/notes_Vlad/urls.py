from django.urls import path
from . import views

urlpatterns = [
    path('', views.NotesVlad.as_view(), name='NotesVlad'),
    path('delete-all/', views.DeleteAllView.as_view(), name='delete_all'),
    path('delete-item/<int:item_id>/', views.DeleteItemView.as_view(), name='delete_item'),
    path('update-item/<int:item_id>/', views.UpdateItemView.as_view(), name='update_item'),
    path('search/', views.SearchNotesView.as_view(), name='search_notes'),
]
