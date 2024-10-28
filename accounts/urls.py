from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="accounts_home"),
    path('register/', views.registration, name="register"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
]