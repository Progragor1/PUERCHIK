from .forms import NoteForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Note,Women

def index(request):
    return HttpResponse(f'{note.title} {note.text} ' for note in Note.objects.all())

def women(request):
    return HttpResponse(f"{women.title} {women.content},Опубликовано: {women.time_create}"
                        f",Изменено:{women.time_update} Работает: {women.is_published}   "
                        for women in Women.objects.all())

def test(request):
    return render(request,'myapp/add_note.html')

def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = NoteForm()
    return render(request,'myapp/add_note.html',{'form': form})

