from django.shortcuts import render, redirect, get_object_or_404
from .models import ToDo
from .forms import TaskForm

def list_all_todos(request):
	todos=ToDo.objects.all()
	return render(request, 'index.html', {'tasks':todos})

def create_a_todo(request):
	if request.method == 'POST':
		this_form=TaskForm(request.POST)
		if this_form.is_valid():
			this_form.save()
			return redirect('mytodos')
	else:
		this_form=TaskForm()
	return render(request, 'todo_form.html', {'form': this_form})

def update_a_todo(request, id):
	todo_to_edit=get_object_or_404(ToDo, id=id)
	if request.method == 'POST':
		this_form=TaskForm(request.POST, instance=todo_to_edit)
		if this_form.is_valid():
			this_form.save()
			return redirect('mytodos')
	else:
		this_form=TaskForm()
	return render(request, 'todo_form.html', {'form': this_form})

def delete_a_todo(request, id):
	todo_to_delete=get_object_or_404(ToDo, id=id)
	todo_to_delete.delete()
	return redirect('mytodos')


