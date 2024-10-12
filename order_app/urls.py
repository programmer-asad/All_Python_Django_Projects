from django.urls import path
from . import views



urlpatterns = [
    path('all_orders/', views.orders),
]