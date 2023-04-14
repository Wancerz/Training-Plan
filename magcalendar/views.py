from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.http import HttpResponse
# Create your views here.


# def say_hello(request):
#     return HttpResponse('Hello Word')

def Main(request):
    x = 1
    y = 2
    return render(request, 'main.html')

def HomePageSite(request):
    x = 1
    y = 2
    return render(request, 'HomePage.html')

@login_required(login_url='LoginSite')
def CalendarSite(request):
    x = 1
    y = 2
    return render(request, 'calendar.html', {'name' : 'Wanat'})





