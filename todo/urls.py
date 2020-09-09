from django.urls import path
from . import views
from todo.models import Task

app_name = "todo"

urlpatterns = [
	path('', views.TaskListView.as_view(), name = 'index'),
	path('saveTask', views.saveTask, name = 'saveTask'),
	path('delete/<int:id>', views.delete, name = 'delete'),
	path('edit/', views.editTask, name = 'editTask'),
]