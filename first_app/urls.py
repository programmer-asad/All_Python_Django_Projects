from django.urls import path
from . import views


urlpatterns = [
    # path('home/', views.say_hello),
    path('', views.home),
    path('about/', views.about),
    path('contact/', views.contact),
    path('service/', views.service),
    path('experiment/', views.experiment),
    path('experiment/<person>', views.experiment),
    path('experiment/<person>/greetings/<greet>', views.experiment_greet),
]