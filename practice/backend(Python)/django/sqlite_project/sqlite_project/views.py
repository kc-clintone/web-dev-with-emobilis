from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm

# ---create a todo---
def create_todo(request):
    if request.method == 'post':
        this_form=TodoForm(request.POST)
        if this_form.is_valid():
            this_form.save()
            return redirect('/')
    else:
        this_form=TodoForm()
    return render(request, 'forms.html',{'form': this_form})

# ---read todos---
def list_todos(request):
    todos=Todo.objects.all()
    return render(request, 'index.html', {'todos': todos})

# ---update todos---
def update_todo(request, _id):
    todo=get_object_or_404(Todo, _id=id)
    if request.method == 'post':
        this_form=TodoForm(request.POST,instance=todo)
        if this_form.is_valid():
            this_form.save()
            return ridirect('/')
    else:
        this_form=TodoForm(instance=todo)
    return render(request, 'forms.html', {'form': this_form})

# ---delete a todo---
def delete_todo(request, _id):
    todo=get_object_or_404(Todo, _id=id)
    todo.delete()