from django.shortcuts import render, reverse
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.views.generic import TemplateView
from .models import Note
from accounts.models import CustomUser
from django.http import HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator
from django.db.models import Q




class NoteDetailView(DetailView):
    model = Note
    context_object_name = 'note'
    template_name = 'notes/note_detail.html'


def NotesList(request):
    user = CustomUser.objects.all().get(username=request.user.username)
    notes = user.usernote.all()
    paginator = Paginator(notes, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    data = {'page_obj': page_obj}
    return render(request, "notes/notes_list.html", context=data)

def NotesSearchList(request):
    user = CustomUser.objects.all().get(username=request.user.username)
    def get_queryset():
        query = request.GET.get('q')
        return user.usernote.filter(
            Q(note_title__icontains=query) | Q(pub_date__icontains=query) | Q(note_text__icontains=query)
        )
    notes = get_queryset()
    paginator = Paginator(notes, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    #data = {'notes_search': get_queryset()}
    data = {'page_obj': page_obj}
    return render(request, 'notes/notes_search_result.html', context=data)



class NoteCreationForm(TemplateView):
    template_name = 'notes/create_note.html'

def NoteCreate(request):
    if request.POST.get('datecheck'):
        Note.objects.create(note_title=request.POST['title'], note_text=request.POST['text'], do_before=request.POST['date'], pub_author=request.user)
    else:
        Note.objects.create(note_title=request.POST['title'], note_text=request.POST['text'],
                            do_before='2099-01-01', pub_author=request.user)

    return HttpResponseRedirect(reverse('notes'))

def ActiveNote(request):
    noteid = request.POST.get('noteid')
    if request.POST.get('activeFalse'):
        Note.objects.filter(id=noteid).update(is_active=False)
    else:
        Note.objects.filter(id=noteid).update(is_active=True)
    return HttpResponseRedirect(noteid)

