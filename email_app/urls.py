from django.urls import path
from . import views


urlpatterns = [
    path('show_email/', views.send_email)
]