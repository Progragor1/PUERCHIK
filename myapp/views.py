from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import *
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import *
from .models import *
from django.apps import apps


class NoteView(APIView):
    def get(self, request):
        id = request.query_params.get("id")
        if id:
            note = Note.objects.get(pk=id)
            return Response({
                "id": note.id,
                "title": note.title,
                "text": note.text
            })
        notes = Note.objects.all()

        return Response(notes.values())

    def post(self, request):
        title = request.data.get("title")
        text = request.data.get("text")
        note = Note.objects.create(title=title, text=text)

        return Response({
            "id": note.id,
            "title": note.title,
            "text": note.text
        })

    def put(self, request):
        id = request.data.get("id")
        if not id:
            return Response({"error": 'Нет id'})

        note = Note.objects.get(pk=id)
        if not note:
            return Response({"error": "Нет такой заметки"})
        title = request.data.get('title')
        text = request.data.get('text')
        note.update(title=title, text=text)

        updated_note = Note.objects.get(pk=id)
        return Response({
            "id": updated_note.id,
            "title": updated_note.title,
            "text": updated_note.text
        })

    def delete(self, request):
        id = request.query_params.get('id')
        if not id:
            return Response({"error": "Нет id"})
        note = Note.objects.get(pk=id)
        if not note:
            return Response({"error": "Нет такой заметки"})
        note.delete()

        return Response({
            "success": "Заметка успешно удалена"
        })


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializerDetail


def index(request):
    user = User.objects.filter(id=request.user.id)
    if len(user) != 0:
        coreModel = apps.get_model('backend', 'Core')
        core = coreModel.objects.get(user=request.user)
        return render(request, 'index.html', {'core': core})
    else:
        return redirect('login')


def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'invalid': True})
    else:
        return render(request, 'login.html', {'invalid': False})


def user_logout(request):
    logout(request)
    return redirect('login')


def user_registration(request):
    coreModel = apps.get_model('backend', 'Core')
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            existing_user = User.objects.filter(username=username)
            if len(existing_user) == 0:
                password = form.cleaned_data['password']
                user = User.objects.create_user(username, '', password)
                user.save()
                login(request, user)
                core = coreModel(user=user)
                core.save()
                return redirect('index')
            else:
                return render(request, 'registration.html', {'invalid': True, 'form': form})
    else:
        form = UserForm()
        return render(request, 'registration.html', {'invalid': False, 'form': form})
