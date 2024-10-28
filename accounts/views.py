# Built-in user creation model


# from django.shortcuts import render, redirect
# from django.http import HttpResponse 
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm

# # Create your views here.


# -------------  1st (first) process -----------

# def registration(request):
#     # return HttpResponse("Registration view")



# -------------  2nd (second)  process -----------

# def registration(request):
#     if request.method == "POST":
#         form = UserCreationForm(data = request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("register")
#     else:    
#         form = UserCreationForm()
#     context = {
#         "form": form,
#     }
#     return render(request, 'accounts/register.html', context = context)





# Custom user creation model
from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout



class CustomUserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
        ]
    


def registration(request):
    if request.method == "POST":
        form = CustomUserCreateForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect("register")
    else:    
        form = CustomUserCreateForm()
    context = {
        "form": form,
    }
    return render(request, 'accounts/register.html', context = context)



def home(request):
    return render(request, 'accounts/home.html')



def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)   
        if form.is_valid(): 
            user = form.get_user()
            login(request, user)
            return redirect("accounts_home")
    else:
        form = AuthenticationForm()
    context = {
        "form": form,
    }
    return render(request, 'accounts/login.html', context=context)



def logout_view(request):
    logout(request)
    return redirect('login')

