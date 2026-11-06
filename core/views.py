from django.shortcuts import render, redirect
from .models import Todolist


def home(request):
    return render(request, 'core/home.html')


def about(request):
    return render(request, 'core/about.html')


def contact(request):
    return render(request, 'core/contact.html')


def todolist(request):
    queryset = Todolist.objects.all()
    completed = Todolist.objects.filter(is_completed=True).count()
    incomplete = Todolist.objects.filter(is_completed=False).count()
    context = {
        'tasks': queryset,
        'completed': completed,
        'incomplete': incomplete,
    }
    return render(request, 'core/todolist.html', context)


def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Todolist.objects.create(title=title, description=description)
        return redirect('todolist')
    return render(request, 'core/create.html')