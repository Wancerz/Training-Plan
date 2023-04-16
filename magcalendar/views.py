from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.http import HttpResponse
# Create your views here.
from django.views.generic import View
from time import time
from django.http import JsonResponse
# def say_hello(request):
#     return HttpResponse('Hello Word')
from magcalendar.models import Exercises, Calendar_exercises
from django.core import serializers
import json
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

    print("AAAAAAA")
    # queryset = Calendar_exercises.objects.all()
    return render(request, 'calendar.html')



def get_data(request):
    text = request.GET.get('button_text')
    print(text)
    print("AAAAAAAAAA")

    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        t = time()
        # print(t)
        print(text+"AAAAAAA")
        queryset = Calendar_exercises.objects.all()

        queryset = serializers.serialize('json',queryset)
        # return JsonResponse({'seconds':t}, status=200)
        # queryset = json.dumps(queryset)
        # toJSON()
        # print(queryset)
        return JsonResponse({'queryset':queryset})

    return render(request,'calendar.html', {'seconds':t, } )


# def get_data(request):
#     text = request.GET.get('button_text')
#     print(text)
#     print("AAAAAAAAAA")

    
#     if request.headers.get('x-requested-with') == 'XMLHttpRequest':
#         t = time()
#         # print(t)
#         print(text+"AAAAAAA")
#         queryset = Calendar_exercises.objects.all()

#         # queryset = serializers.serialize('json',queryset)
#         # return JsonResponse({'seconds':t}, status=200)
#         return JsonResponse({'seconds':t, 'queryset':list(queryset)}, status=200)

#     return render(request,'calendar.html', {'seconds':t, } )
