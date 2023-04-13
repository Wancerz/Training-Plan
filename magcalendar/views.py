from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# Create your views here.


# def say_hello(request):
#     return HttpResponse('Hello Word')


def say_hello(request):
    x = 1
    y = 2
    return render(request, 'calendar.html', {'name' : 'Wanat'})


def mainsite(request):
    x = 1
    y = 2
    return render(request, 'main.html')