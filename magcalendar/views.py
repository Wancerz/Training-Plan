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
from datetime import datetime
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
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

def show_day_calendar(request):
    date = request.GET.get('date')
    date = date[4:]
    date = datetime.strptime(date,"%b %d %Y").date()
    print(date)
    

    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':

        
        queryset = Calendar_exercises.objects.filter(created_at=date).filter(id_User_id=request.user.id).select_related('id_Exercises').values('note','repeats','id_Exercises__title' )

    # for exercise in queryset:
    #     print(f"Exercise: {exercise.id_Exercises.title}")
    #     print(f"Note: {exercise.note}")
    #     print(f"Repeats: {exercise.repeats}")

        # queryset = list(queryset)
        # queryset = serializers.serialize('json',queryset)
        print(queryset)
        queryset = json.dumps(list(queryset))
        # return JsonResponse({'seconds':t}, status=200)
        # queryset = json.dumps(queryset)
        # toJSON()
        # print(queryset)
        return JsonResponse({'queryset':queryset})

    return render(request,'calendar.html' )

#coś pomieszałem tutaj i jako repeats wysyła się z fronute note i vice versa
def delete_row(request):
     exercise = request.GET.get('exercise')
     repeats = request.GET.get('note')
     note = request.GET.get('repeats')
     date = request.GET.get('date')
     date = date[4:]
     date = datetime.strptime(date,"%b %d %Y").date()
     if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        print("EXERCISE",exercise)
        print("repeats",repeats)
        print("note",note)
        print(date)
        queryset = Calendar_exercises.objects.filter(created_at=date, note=note, repeats=repeats, id_Exercises__title=exercise, id_User_id=request.user.id)[0]
        queryset.delete()

     return render(request,'calendar.html' )
    


def add_values_to_options(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':

        queryset = Exercises.objects.values('title')


        for query in queryset:
            print(query)
        queryset = json.dumps(list(queryset))
        
        print(queryset)
        return JsonResponse({'queryset':queryset})


    return render(request,'calendar.html')


def add_exercise_to_db(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        exercise = request.GET.get('exerc')
        note = request.GET.get('not')
        rep = request.GET.get('rep')
        date = request.GET.get('currentDate')
        date = date[4:]
        date = datetime.strptime(date,"%b %d %Y").date()
        
        exercise = Exercises.objects.get(title=exercise)
        queryset = Calendar_exercises(note=note, repeats=rep, id_Exercises=exercise, id_User_id = request.user.id, created_at=date)
        queryset.save()
        # queryset = Exercises.objects.values('title')
    



    return render(request,'calendar.html')















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
