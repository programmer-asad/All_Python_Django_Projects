from django.urls import path
from .views import hello, task_list, task_detail
from .views import Task_list, TaskDetail, TaskViewSet, AuthorViewSet, BookViewSet
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('home/', hello),
#     path('tasks/', task_list),
#     path('tasks/<int:pk>/', task_detail),
    
    # path('tasks/', Task_list.as_view()),
    # path('tasks/<int:pk>/', TaskDetail.as_view()),
]


router = DefaultRouter()
router.register('tasks', TaskViewSet, basename= 'task')
router.register('authors', AuthorViewSet, basename= 'author')
router.register('books', BookViewSet, basename= 'book')
urlpatterns += router.urls

