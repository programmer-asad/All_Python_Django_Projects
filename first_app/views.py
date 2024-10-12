from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def say_hello(request):
    return HttpResponse("Hello Django!!!")


# def homepage(request):
#     return HttpResponse("Welcome to Homepage content")


def homepage(request):
    data = {"name": "Ostad"}
    return render(request, 'index.html', context = data)



def about(request):
    return render(request, 'about.html')



def contact(request):
    return render(request, 'contact.html')



def service(request):
    return render(request, 'service.html')



def global_home(request):
    return render(request, 'global_home.html')
