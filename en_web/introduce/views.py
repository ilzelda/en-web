from django.shortcuts import render, redirect
from .models import Todo
from django.utils import timezone

# Create your views here.

def showHome(request):
    return render(request, 'home.html')

def createTodo(request):
    if (request.method == 'POST'):
        new_Todo = Todo()
        new_Todo.title = request.POST['title']
        new_Todo.date = timezone.now()
        new_Todo.progress = 0

        new_Todo.save()
    return redirect('home')