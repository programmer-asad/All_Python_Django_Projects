from django.urls import path
from . import views



urlpatterns = [
    path('all_order/', views.orders)
] 