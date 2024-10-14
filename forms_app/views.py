from django.shortcuts import render, redirect
from .models import Task
from django.http import HttpResponse
from .forms import TaskForm


# Create your views here.



def task_list(request):
    tasks = Task.objects.all()
    completed = request.GET.get("completed")
    if completed == '1':
        tasks = tasks.filter(completed = True)
    elif completed == '0':
        tasks = tasks.filter(completed = False)
    return render(request, 'task_list.html', {"tasks": tasks})



def task_details(request, pk):
    task = Task.objects.get(pk=pk)
    return render(request, 'task_detail.html', {"task":task})




# manually add, delete and update task

def add_task(request):
    # return HttpResponse("Adding task")
    _title = "Let's go for walk"
    _description = "Walking is a good exercise for health"
    _completed = False
    _due_date = "2024-10-14"
    
    task = Task(title = _title, description = _description, completed = _completed, due_date = _due_date)
    task.save() 
    return redirect('task_list')



def delete_task(request, pk):
    # return HttpResponse("Deleting Task number " + str(pk))
    try:
        task = Task.objects.get(pk=pk)
        task.delete()
        return redirect('task_list')
    except Task.DoesNotExist:
        return HttpResponse("Task Does not exist")
    
    
    
def update_task(request): 
    task = Task.objects.get(pk = 3)
    task.title = "This is a modified title";
    task.save()
    return redirect('task_list')





# with form add, delete and update task

def add_task_form(request):
    # return HttpResponse("Adding form")
    
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('task_list')
    else:
        form = TaskForm()      
        return render(request, 'add_task_form.html', {"form": form})





