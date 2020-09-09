from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from todo.models import Task

class TaskListView (ListView):
	model = Task
	context_object_name = 'tasks'
	template_name = 'todo/index.html'

	def get_queryset(self):
		queryset = Task.objects.order_by('date_added')[:10]
		return queryset

def saveTask(request):
	if request.method == 'POST':
		task = request.POST.get('task')
		task = Task(name = task)
		task.save()
		return redirect('todo:index')

def delete(request, id):
	task = Task.objects.get(id=id)
	task.delete()
	return redirect('todo:index')


def editTask(request):
	if request.method == 'POST':
		taskId = request.POST.get('id')
		task = request.POST.get('task')
		taskObj = Task.objects.get(id=taskId)
		taskObj.name = task
		taskObj.save()
		return redirect('todo:index')

