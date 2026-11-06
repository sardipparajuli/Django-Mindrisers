from django.shortcuts import render, redirect, get_object_or_404
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


def mark_complete(request, id):
    task = get_object_or_404(Todolist, id=id)
    # if is_completed is True -> False and if is_completed is False -> True
    task.is_completed = not task.is_completed
    task.save()
    return redirect('todolist')


def edit(request, id):
    task = get_object_or_404(Todolist, id=id)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.save()
        return redirect('todolist')

    context = {'task': task}
    return render(request, 'core/edit.html', context)