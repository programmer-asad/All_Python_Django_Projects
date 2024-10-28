from django.urls import path
from . import views



urlpatterns = [
    path('add/', views.add_task_form, name= 'add'),
    path('', views.task_list, name="task_list"),
    path('task_details/<int:pk>', views.task_details, name="detail"),
    path('delete/<int:pk>', views.delete_task, name="delete_tsk"),
    path('update/<int:pk>', views.update_task, name="update_tsk"),
    path('user/<int:user_id>', views.task_by_user_id, name="user_tasks"),
    path('books/', views.all_books, name="all_books"),
    path('books/<int:book_id>', views.book, name="book"),
    path('author/<int:author_id>', views.author, name="author"),
]