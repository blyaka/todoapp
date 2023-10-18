from django.urls import path
from .views import NoteDetailView, NoteCreationForm, NoteCreate, NotesList, ActiveNote, NotesSearchList

urlpatterns = [
    #path('', AllNotesListView.as_view(), name='notes'),
    path('', NotesList, name='notes'),
    path('<uuid:pk>/', NoteDetailView.as_view(), name = 'note'),
    path('notecreationform/', NoteCreationForm.as_view(), name='notecreationform'),
    path('notecreate', NoteCreate, name='notecreate'),
    path('active-note', ActiveNote, name='active-note'),
    path('search/', NotesSearchList, name='notes_search'),
]