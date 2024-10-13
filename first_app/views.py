from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# def say_hello(request):
#     return HttpResponse("Welcome to Django")


def home(request):
    page = {
            'title': 'Homepage AWESOME!!!',
           'content': 'Welcome to Homepage'
           }
    return render(request, 'index.html', context = page)


def about(request):
    return render(request, 'about.html')


def contact(request):
    email = 'contact@gmail.com'
    
    socila_profiles = [
        "Facebook: facebook.com/profile",
        "Youtube: youtube.com/channelid",
        "Instagram: Instagram.com/profile",
        "Twitter: twitter.com/profile",
        "Pinterest: pinterest.com/profile",
        "Redit: redit.com/profile"
        
    ]
    hq = "k"
    return render(request, 'contact.html', {"email_address": email, "socialprofiles": socila_profiles, "hq":hq})



def service(request):
    return render(request, 'service.html')



def experiment(request, person=None):
    if person is None:
        person = "Guest"
    return render(request, 'experiment.html', {"data": person})



def experiment_greet(request, person, greet):
    return render(request, 'experiment.html', {"data": person, "greetings": greet})



# def experiment_greet(request, person, greet=None):
#     if greet is None:
#         greet = "What's up"
#     return render(request, 'experiment.html', {"data": person, "greetings": greet})




