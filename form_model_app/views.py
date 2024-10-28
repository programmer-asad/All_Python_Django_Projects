from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Task, Book, Author
from .forms import TaskForm
from django.forms.models import model_to_dict

from django.contrib.auth.models import User


# Create your views here.


# create form
def add_task_form(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
        else:
            return render(request, 'add_form.html', {'form': form})             
    else:
        form = TaskForm()
        return render(request, 'add_form.html', {'form': form})
    
    
    
# read form all data    
def task_list(request):
    tasks = Task.objects.all()
    
    completed = request.GET.get('completed')
    if completed == '1':
        tasks = tasks.filter(completed=True)
    elif completed == '0':
        tasks = tasks.filter(completed=False)
    
    return render(request, 'task_list.html', {"tasks": tasks})



# read form single data  
def task_details(request, pk):
    try:
        task = Task.objects.get(pk = pk)
        return render(request, 'task_detail.html', {"task": task})
    except Task.DoesNotExist:
        return HttpResponse("Task does not exist")
    
    
    
# delete data      
def delete_task(request, pk):
    try:
        del_task = Task.objects.get(pk = pk)
        del_task.delete()
        return redirect('task_list')
    except Task.DoesNotExist:
        return HttpResponse("Task does not exist")
    
    
    
            # --------------update data---------------------
# Process: 1
# def update_task(request, pk):
#     return HttpResponse("Update task form")



# Process: 2
# def update_task(request, pk):
#     return HttpResponse("Update task form: " + str(pk))



# Process: 3,  data invoke from database, send invoked data to form, show form in html
# def update_task(request, pk):
#     try:
#         updated_task = Task.objects.get(pk = pk)
#         updated_task_form = TaskForm(instance=updated_task)
#         return render(request, "update_task.html", {"form_update": updated_task_form})
#     except Task.DoesNotExist:
#         return HttpResponse("Task does not exist")




# Process: 4,  update data 
def update_task(request, pk):
    try:
        updated_task = Task.objects.get(pk = pk)
            
        if request.method == "POST":
            task_form = TaskForm(request.POST, instance=updated_task)
            if task_form.is_valid():
                task_form.save()
                return redirect("task_list")
            else:
                context = {
                    "form_update": updated_task_form
                }
                return render(request, "update_task.html", context = context)
                                  
        updated_task_form = TaskForm(instance=updated_task)
        return render(request, "update_task.html", {"form_update": updated_task_form})
       
    except Task.DoesNotExist:
        return HttpResponse("Task does not exist")
    
    
    
    
# def task_by_user_id(request, user_id):
    # ------------ Process: 1  ---------------
    # tasks = Task.objects.filter(user_id=user_id).values()
    # return JsonResponse({"tasks":list(tasks)})
    
    
    
    # ------------ Process: 2  ---------------
    # def task_by_user_id(request, user_id):
    # tasks = Task.objects.filter(user_id=user_id)
    # result = []
    # for task in tasks:
    #     result.append({
    #         "title": task.title,
    #         "description": task.description,
    #         "completed": task.completed,
    #         "due_date": task.due_date,
    #         "user_id": task.user.id,
    #         "user": task.user.username
    #     })
        
    # return JsonResponse({"tasks":result})




     # ------------ Process: 3  ---------------
     
def task_by_user_id(request, user_id):
    user = User.objects.get(pk=user_id)
    tasks = user.tasks.all().values()    
    # tasks = user.task_set.all()    # if related_name is not said then "task_set".
    return JsonResponse({"tasks": list(tasks)})





#  ============== Books and Author Relationship =================

def all_books(request):
    books = Book.objects.all()
    # return JsonResponse({"books": list(books)})
    result = []
    for book in books:
        result.append({
        "title": book.title,
        "description": book.description,
        "publication_date": book.publication_date,
        "author": f'{book.author.first_name} {book.author.last_name}'
        })
    return JsonResponse({"books":result})


# def book(request, book_id):
#     book = Book.objects.get(pk = book_id)    
#     # book_to_json = model_to_dict(book)
#     book_details ={
#         "title": book.title,
#         "description": book.description,
#         "publication_date": book.publication_date,
#         "author": f'{book.author.first_name} {book.author.last_name}'
#     }
#     return JsonResponse({"book": book_details})



def author(request, author_id):
    author = Author.objects.get(pk = author_id)
    author_details = {
        "first_name": author.first_name,
        "last_name": author.last_name,
        "bio": author.bio,
        "books": [book.title for book in author.book_set.all()] 
    }
    return JsonResponse({"author": author_details})




# ----------  Many to Many ---------

def book(request, book_id):
    book = Book.objects.get(pk = book_id)    
    # book_to_json = model_to_dict(book)
    book_details ={
        "title": book.title,
        "description": book.description,
        "publication_date": book.publication_date,
        "author": [
             f'{author.first_name} {author.last_name}' 
             for author in book.author.all()
        ],           
    }
    return JsonResponse({"book": book_details})


def all_books(request):
    books = Book.objects.all()
    # return JsonResponse({"books": list(books)})
    result = []
    for book in books:
        result.append({
        "title": book.title,
        "description": book.description,
        "publication_date": book.publication_date,
        
        # "author_ids": [
        #      author.id for author in book.author.all()
        # ],
        # "author": [f'{author.first_name} {author.last_name}'
        #            for author in book.author.all()
        #            ]
        
        "authors":[
            {
                "id": author.id,
                "first_name": author.first_name,
                "last_name": author.last_name,              
            }
             for author in book.author.all()
        ]
        
        })
    return JsonResponse({"books":result})
        
