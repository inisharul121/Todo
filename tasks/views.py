from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import TaskForm
# Create your views here.
def task (request):

    task_list=Task.objects.all()
    form=TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')


    context={'task_list':task_list,'form':form}
    return render(request, 'tasks/task.html',context)


def updateTask(request,pk):

    taskupdate=Task.objects.get(id=pk)
    form = TaskForm(instance=taskupdate)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=taskupdate)
        if form.is_valid():
            form.save()
            return redirect('/')


    context = {'taskupdate': taskupdate, 'form': form}
    return render(request, 'tasks/update.html', context)

def deleteTask(request,pk):

    item=Task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context = {'item': item}
    return render(request, 'tasks/delete.html', context)
