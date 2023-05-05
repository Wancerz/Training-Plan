from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .forms import SignUpForm,LogInForm
from django.contrib import messages
from magcalendar import views as magv
from django.contrib.auth.decorators import login_required
# from magcalendar import say_hello as 
# Create your views here.


def register(request):
    if request.user.is_authenticated:
         return redirect("CalendarSite")
    else:

        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'Account was created for ' + user)
                return redirect('LoginSite')

        else:
                form = SignUpForm()

    context = {'form':form
    }
    return render(request, "register/register.html", context)



def LoginSite(request):
    
    if request.user.is_authenticated:
         return redirect("CalendarSite")
    else:
        if request.method == 'POST':
            form = LogInForm(request.POST)
            username = request.POST.get('username')
            password = request.POST.get('password1')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("CalendarSite")
            else:
                messages.info(request, "Username or password is incorrect")
        else:
            form = LogInForm()

    context = {
         'form':form
    }
    return render(request, "login/login.html", context)


def LogoutSite(request):
     logout(request)
     return redirect('LoginSite')