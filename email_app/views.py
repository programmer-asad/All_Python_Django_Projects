from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def send_email(request):
    # return HttpResponse("This is the email management system")
    return render(request, 'email.html')
