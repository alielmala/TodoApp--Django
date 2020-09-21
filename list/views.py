from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.
def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    
    
    if request.method== 'POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context= {'tasks':tasks,'form':form}     
    return render(request,'list/home.html',context)

def editTask(request, pk):
    task = Task.objects.get(id=pk)
    form = EditTask(instance=task)
    if request.method== 'POST':
        form = EditTask(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'form': form}
    return render(request,'list/task_edit.html',context)

def deleteTask(request, pk):
    item = Task.objects.get(id=pk)
    if request.method== 'POST':
        item.delete()
        return redirect('/')
    context={'item':item}   
    return render (request, 'list/delete.html',context)