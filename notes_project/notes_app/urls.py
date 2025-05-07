from django.urls import path
from . import views, admin

urlpatterns = [
    path('', views.notes_list, name='notes_list'),
    path('notes_list/', views.notes_list, name='notes_list'),
    path('note_detail/<int:pk>/', views.note_detail, name='note_detail'),
    path('add_note/', views.add_note, name='add_note'),
    path('note/<int:pk>/note_form/', views.note_edit, name='note_edit'),
    path('note/<int:pk>/delete/', views.note_delete, name='note_delete'),
]