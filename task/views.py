from django.shortcuts import render,redirect
from . import forms
from task.models import Task

# Create your views here.
def add_task(request):
    if request.method == 'POST':
        task_form = forms.TaskFrom(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('add_task')
    else:
        task_form = forms.TaskFrom()
    return render(request,'tasks/add_task.html',{'form':task_form})


def edit_task(request,id):
    task = Task.objects.get(pk=id)
    task_form = forms.TaskFrom(instance=task)
    # print(tak.taskTitle)
    if request.method == 'POST':
        task_form = forms.TaskFrom(request.POST,instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect('show_tasks')
    return render(request,'tasks/add_task.html',{'form':task_form})


def delete_task(request,id):
    task = Task.objects.get(pk=id)
    task.delete()
    return redirect('show_tasks')


def show_tasks(request):
    data = Task.objects.all()
    # print(data)
    return render(request,'tasks/show_tasks.html',{'data':data})
