from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Task

def home(request):
    tasks = Task.objects.all().order_by('-created_date')
    return render(request, 'home.html', {'tasks': tasks})

def add(request):
    if request.method == 'POST':
        title = request.POST['title']
        task = Task(title=title)
        task.save()
        return redirect('home')
    else:
        return render(request, 'add.html')

def delete(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('home')

def complete(request, pk):
    task = Task.objects.get(pk=pk)
    task.completed = True
    task.save()
    return redirect('home')
