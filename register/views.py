from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .forms import SignUpForm,LogInForm
from django.contrib import messages
# Create your views here.


def register(request):
    # print(request.POST)
    


    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was created for' + user)
            return redirect('login')

    else:
            # print(form.errors)
            form = SignUpForm()

    context = {'form':form
    }
    return render(request, "register/register.html", context)



def LoginSite(request):
    print(request.POST)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, passowrd=password)

        if user is not None:
             login(request, user)
             redirect('calendar')

    # if request.method == 'POST':
    #     form = SignUpForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('/')

    # else:
    #         # print(form.errors)
    #         form = SignUpForm()
    form = LogInForm()
    context = {'form':form
    }
    return render(request, "login/login.html", context)